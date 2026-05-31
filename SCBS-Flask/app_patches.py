# ============================================================
# PATCH 1 — Replace your existing /admin dashboard route
# with this version. It adds iso_start and iso_end fields
# that the JS countdown needs.
# ============================================================

from datetime import datetime, timedelta
import re

# ── Time-parsing helpers ─────────────────────────────────────
_MONTH_MAP = {
    'january':1,'february':2,'march':3,'april':4,
    'may':5,'june':6,'july':7,'august':8,
    'september':9,'october':10,'november':11,'december':12,
}

def parse_booking_date(date_str):
    """
    Accepts multiple date formats and returns a datetime.date object.
    Supported:
      - "YYYY-MM-DD"          (SQLite default)
      - "Month DD, YYYY"      (e.g. "April 29, 2026")
    """
    date_str = date_str.strip()

    # ISO format
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        pass

    # "Month DD, YYYY"
    m = re.match(
        r'^(\w+)\s+(\d{1,2}),\s+(\d{4})$', date_str, re.IGNORECASE
    )
    if m:
        month_num = _MONTH_MAP.get(m.group(1).lower())
        if month_num:
            return datetime(int(m.group(3)), month_num, int(m.group(2))).date()

    raise ValueError(f"Unrecognised date format: {date_str!r}")


def parse_time_str(time_str):
    """
    Accepts 12-hr or 24-hr time strings and returns a datetime.time object.
    Supported:
      - "HH:MM"       (24-hr, no seconds)
      - "HH:MM:SS"    (24-hr, with seconds)
      - "HH:MM AM/PM" (12-hr)
    """
    time_str = time_str.strip()
    for fmt in ("%I:%M %p", "%H:%M:%S", "%H:%M"):
        try:
            return datetime.strptime(time_str, fmt).time()
        except ValueError:
            continue
    raise ValueError(f"Unrecognised time format: {time_str!r}")


def build_iso(date_str, time_str):
    """Returns an ISO-8601 string like '2026-04-29T14:00' for JS Date()."""
    d = parse_booking_date(date_str)
    t = parse_time_str(time_str)
    return datetime(d.year, d.month, d.day, t.hour, t.minute, t.second).strftime("%Y-%m-%dT%H:%M:%S")


# ── Dashboard route ──────────────────────────────────────────
@app.route('/admin', methods=['GET', 'POST'])
def dashboard():

    if request.method == 'POST':
        email    = request.form.get('email')
        password = request.form.get('password')

        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur  = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email = ? AND role = 'admin'", (email,))
        admin = cur.fetchone()
        conn.close()

        if admin and check_password_hash(admin['password'], password):
            session['admin'] = admin['email']
            return redirect(url_for('dashboard'))

        return render_template('auth/admin-login.html', error="Invalid admin credentials")

    if 'admin' not in session:
        return render_template('auth/admin-login.html')

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM reservations")
    reservations_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM categories")
    categories_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM facilities")
    facilities_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM users")
    users_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM inquiries")
    inquiries_count = cur.fetchone()[0]

    cur.execute("SELECT IFNULL(SUM(total_amount), 0) FROM reservations WHERE status = 'Approved'")
    total_sales = cur.fetchone()[0]

    cur.execute("""
        SELECT
            r.id, r.booking_date, r.start_time, r.end_time, r.status,
            r.facility_id, r.user_id,
            u.name  AS user_name,
            f.name  AS facility_name,
            c.name  AS category_name
        FROM reservations r
        LEFT JOIN users      u ON r.user_id      = u.id
        LEFT JOIN facilities f ON r.facility_id  = f.id
        LEFT JOIN categories c ON f.category_id  = c.id
        WHERE r.status = 'Approved'
        ORDER BY r.id DESC
    """)
    active_rows = cur.fetchall()
    conn.close()

    active_reservations = []
    for r in active_rows:
        row = dict(r)
        try:
            row['iso_start'] = build_iso(row['booking_date'], row['start_time'])
            row['iso_end']   = build_iso(row['booking_date'], row['end_time'])
        except Exception as e:
            print(f"[dashboard] date parse error for reservation {row['id']}: {e}")
            row['iso_start'] = ''
            row['iso_end']   = ''
        active_reservations.append(row)

    return render_template(
        'admin/dashboard.html',
        active_page='dashboard',
        reservations_count=reservations_count,
        categories_count=categories_count,
        facilities_count=facilities_count,
        users_count=users_count,
        inquiries_count=inquiries_count,
        total_sales=total_sales,
        active_reservations=active_reservations,
    )


# ============================================================
# PATCH 2 — Replace your existing /extend_reservation route.
# Now accepts plain integer `minutes` instead of a string.
# Also returns `new_iso_end` so JS can update without reload.
# ============================================================

@app.route('/extend_reservation', methods=['POST'])
def extend_reservation():
    try:
        data           = request.get_json()
        reservation_id = data.get('reservation_id')
        minutes        = data.get('minutes')   # integer: 30 | 60 | 90 | 120

        # Accept both int and legacy string values
        if isinstance(minutes, str):
            minutes = {'30 mins': 30, '1 hour': 60}.get(minutes)
        minutes = int(minutes) if minutes else None

        if not minutes or minutes <= 0:
            return jsonify({'status': 'error', 'message': 'Invalid duration.'}), 400

        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur  = conn.cursor()

        cur.execute(
            "SELECT booking_date, start_time, end_time FROM reservations WHERE id = ?",
            (reservation_id,)
        )
        row = cur.fetchone()

        if not row:
            conn.close()
            return jsonify({'status': 'error', 'message': 'Reservation not found.'}), 404

        # Parse current end datetime
        try:
            current_end = datetime.combine(
                parse_booking_date(row['booking_date']),
                parse_time_str(row['end_time'])
            )
        except Exception as e:
            conn.close()
            return jsonify({'status': 'error', 'message': f'Date parse error: {e}'}), 500

        new_end          = current_end + timedelta(minutes=minutes)
        new_end_time     = new_end.strftime('%I:%M %p')      # "02:30 PM"
        new_booking_date = new_end.strftime('%Y-%m-%d')       # keep ISO for DB
        new_iso_end      = new_end.strftime('%Y-%m-%dT%H:%M:%S')  # for JS

        cur.execute("""
            UPDATE reservations
            SET end_time = ?, booking_date = ?, date_updated = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (new_end_time, new_booking_date, reservation_id))
        conn.commit()
        conn.close()

        return jsonify({
            'status':       'success',
            'message':      f'Session extended by {minutes} minutes.',
            'new_end_time': new_end_time,
            'new_iso_end':  new_iso_end,
            'new_date':     new_booking_date,
        })

    except Exception as e:
        print('EXTEND ERROR:', e)
        return jsonify({'status': 'error', 'message': str(e)}), 500


# ============================================================
# PATCH 3 — Add this NEW /end_reservation route.
# The dashboard "End" button calls this endpoint.
# ============================================================

@app.route('/end_reservation', methods=['POST'])
def end_reservation():
    try:
        data           = request.get_json()
        reservation_id = data.get('reservation_id')

        if not reservation_id:
            return jsonify({'status': 'error', 'message': 'Missing reservation ID.'}), 400

        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur  = conn.cursor()

        cur.execute("SELECT id, status FROM reservations WHERE id = ?", (reservation_id,))
        row = cur.fetchone()

        if not row:
            conn.close()
            return jsonify({'status': 'error', 'message': 'Reservation not found.'}), 404

        if row['status'] != 'Approved':
            conn.close()
            return jsonify({'status': 'error', 'message': 'Only approved sessions can be ended.'}), 400

        cur.execute("""
            UPDATE reservations
            SET status = 'Completed', date_updated = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (reservation_id,))
        conn.commit()
        conn.close()

        return jsonify({'status': 'success', 'message': 'Session marked as Completed.'})

    except Exception as e:
        print('END RESERVATION ERROR:', e)
        return jsonify({'status': 'error', 'message': str(e)}), 500
