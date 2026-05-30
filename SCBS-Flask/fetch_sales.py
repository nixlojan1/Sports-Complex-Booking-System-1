from flask import Blueprint, jsonify, request
import sqlite3
import os
from datetime import date
from calendar import monthrange

# ======================
# Blueprint
# ======================
fetch_sales = Blueprint('fetch_sales', __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, 'database.db')


# ======================
# DATE RANGE HELPER
# ======================
def resolve_date_range(period, from_date=None, to_date=None):
    """Return (start_str, end_str) ISO dates for the requested period, or (None, None) for all-time."""
    today = date.today()

    if period == 'this_month':
        start = date(today.year, today.month, 1)
        end   = today

    elif period == 'last_month':
        y, m = (today.year, today.month - 1) if today.month > 1 else (today.year - 1, 12)
        start = date(y, m, 1)
        end   = date(y, m, monthrange(y, m)[1])

    elif period == 'last_3_months':
        m = today.month - 3
        y = today.year
        if m <= 0:
            m += 12
            y -= 1
        start = date(y, m, 1)
        end   = today

    elif period == 'this_year':
        start = date(today.year, 1, 1)
        end   = today

    elif period == 'custom' and from_date and to_date:
        try:
            start = date.fromisoformat(from_date)
            end   = date.fromisoformat(to_date)
        except ValueError:
            return None, None

    else:                          # 'all' or unrecognized
        return None, None

    return str(start), str(end)


def date_clause(start, end, col='booking_date'):
    """Return (sql_fragment, params_list) for optional date filtering."""
    if start and end:
        return f"AND {col} BETWEEN ? AND ?", [start, end]
    return "", []


# ======================
# GET SALES SUMMARY
# ======================
@fetch_sales.route('/get_sales_summary')
def get_sales_summary():
    period    = request.args.get('period', 'all')
    from_date = request.args.get('from', '')
    to_date   = request.args.get('to',   '')

    start, end          = resolve_date_range(period, from_date, to_date)
    where_frag, params  = date_clause(start, end)

    conn   = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # ── Approved sales totals ──────────────────────────
    cursor.execute(f"""
        SELECT
            COUNT(*)                        AS total_bookings,
            COALESCE(SUM(total_amount),   0) AS total_revenue,
            COALESCE(AVG(total_amount),   0) AS avg_amount,
            COALESCE(SUM(deposit_amount), 0) AS total_deposits
        FROM reservations
        WHERE status = 'Approved'
        {where_frag}
    """, params)
    row = dict(cursor.fetchone())

    # ── Pending count ──────────────────────────────────
    cursor.execute(f"""
        SELECT COUNT(*) AS pending
        FROM reservations
        WHERE status = 'Pending'
        {where_frag}
    """, params)
    row['pending_count'] = cursor.fetchone()['pending']

    conn.close()
    return jsonify(row)


# ======================
# MONTHLY REVENUE (current year)
# ======================
@fetch_sales.route('/get_sales_by_month')
def get_sales_by_month():
    year = request.args.get('year', str(date.today().year))

    conn   = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            CAST(strftime('%m', booking_date) AS INTEGER) AS month,
            COUNT(*)                                       AS count,
            COALESCE(SUM(total_amount), 0)                 AS revenue
        FROM reservations
        WHERE status = 'Approved'
          AND strftime('%Y', booking_date) = ?
        GROUP BY strftime('%m', booking_date)
        ORDER BY month
    """, (year,))

    rows = {row['month']: dict(row) for row in cursor.fetchall()}
    conn.close()

    MONTHS = ['Jan','Feb','Mar','Apr','May','Jun',
              'Jul','Aug','Sep','Oct','Nov','Dec']

    result = [
        {
            'month':   MONTHS[i],
            'count':   rows.get(i + 1, {}).get('count',   0),
            'revenue': rows.get(i + 1, {}).get('revenue', 0),
        }
        for i in range(12)
    ]
    return jsonify(result)


# ======================
# REVENUE BY FACILITY
# ======================
@fetch_sales.route('/get_sales_by_facility')
def get_sales_by_facility():
    period    = request.args.get('period', 'all')
    from_date = request.args.get('from', '')
    to_date   = request.args.get('to',   '')

    start, end         = resolve_date_range(period, from_date, to_date)
    where_frag, params = date_clause(start, end)

    conn   = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT
            f.name                          AS facility_name,
            COUNT(r.id)                     AS bookings,
            COALESCE(SUM(r.total_amount), 0) AS revenue
        FROM reservations r
        LEFT JOIN facilities f ON r.facility_id = f.id
        WHERE r.status = 'Approved'
        {where_frag}
        GROUP BY r.facility_id
        ORDER BY revenue DESC
    """, params)

    rows         = [dict(r) for r in cursor.fetchall()]
    total_rev    = sum(r['revenue'] for r in rows) or 1  # avoid div/0

    for r in rows:
        r['pct'] = round(r['revenue'] / total_rev * 100, 1)

    conn.close()
    return jsonify(rows)


# ======================
# SALES TRANSACTIONS
# ======================
@fetch_sales.route('/get_sales_transactions')
def get_sales_transactions():
    period    = request.args.get('period',  'all')
    from_date = request.args.get('from',    '')
    to_date   = request.args.get('to',      '')
    search    = request.args.get('search',  '').lower().strip()

    start, end         = resolve_date_range(period, from_date, to_date)
    where_frag, params = date_clause(start, end)

    conn   = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT
            r.id, r.booking_date, r.start_time, r.end_time,
            r.total_amount, r.deposit_amount,
            r.gcash_reference, r.status, r.date_created,
            u.name  AS user_name,
            u.email AS user_email,
            f.name  AS facility_name
        FROM reservations r
        LEFT JOIN users u ON r.user_id = u.id
        LEFT JOIN facilities f ON r.facility_id = f.id
        WHERE r.status = 'Approved'
        {where_frag}
        ORDER BY r.id DESC
    """, params)

    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()

    if search:
        rows = [
            r for r in rows
            if search in str(r.get('user_name',    '')).lower()
            or search in str(r.get('facility_name','')). lower()
            or search in str(r.get('booking_date', '')).lower()
            or search in str(r.get('gcash_reference','')).lower()
        ]

    return jsonify(rows)
