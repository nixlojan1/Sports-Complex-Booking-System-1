import os
import re
import sqlite3
from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, url_for, session, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from fetch_users import fetch_user
from fetch_inquiries import fetch_inquiry
from fetch_categories import fetch_categories
from fetch_facility import fetch_facility
from fetch_reservations import fetch_reservations
from create_reservation import create_reservation
from chatbot import chatbot
from email_notifications import EmailNotification
from process_forgot_password import forgot_password, reset_password, create_reset_tokens_table

# ======================
# BASE DIRECTORY
# ======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))
app.secret_key = 'your_secret_key_here'

# ======================
# BLUEPRINTS
# ======================
app.register_blueprint(fetch_user)
app.register_blueprint(fetch_inquiry)
app.register_blueprint(fetch_categories)
app.register_blueprint(fetch_facility)
app.register_blueprint(fetch_reservations)
app.register_blueprint(create_reservation)
app.register_blueprint(chatbot)

# ======================
# FORGOT PASSWORD ROUTES
# ======================
create_reset_tokens_table()
app.add_url_rule("/forgot-password", view_func=forgot_password, methods=["POST"])
app.add_url_rule("/reset-password",  view_func=reset_password,  methods=["GET", "POST"])

# ======================
# DATABASE CONNECTION
# ======================
db_path = os.path.join(BASE_DIR, 'database.db')
conn = sqlite3.connect(db_path, check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

email_service = EmailNotification(
    sender_email="sportscomplexx1@gmail.com",
    sender_password="kaiu ouav fgqv kfsa"
)


# ======================
# EMAIL HELPER
# ======================
def build_email(title, name, body_html):
    """
    Wraps any email body in the standard Sports Complex card template.
    """
    return f"""
    <div style="font-family: 'Poppins', Arial, sans-serif; max-width: 520px;
                margin: 0 auto; padding: 30px; border-radius: 12px;
                border: 1px solid #e0e0e0; background: #ffffff;">

        <h2 style="color: #205072; margin-bottom: 8px;">{title}</h2>

        <p style="color: #555; font-size: 14px; line-height: 1.6;">
            Hi <strong>{name}</strong>,
        </p>

        {body_html}

        <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">

        <p style="color: #aaa; font-size: 11px; text-align: center;">
            © 2026 Sports Complex Booking System
        </p>
    </div>
    """


# ======================
# CREATE TABLES
# ======================
def init_db():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        facility_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        booking_date TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        total_amount REAL NOT NULL,
        deposit_amount REAL NOT NULL,
        payment_method TEXT DEFAULT 'GCash',
        gcash_reference TEXT,
        payment_screenshot TEXT,
        status TEXT DEFAULT 'Pending',
        purpose TEXT,
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        date_updated TIMESTAMP,
        FOREIGN KEY (facility_id) REFERENCES facilities(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        phone TEXT,
        address TEXT,
        role TEXT DEFAULT 'user',
        status TEXT DEFAULT 'active',
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        profile_image TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL,
        status TEXT DEFAULT 'unread',
        remarks TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'Available',
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS facilities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        category_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        description TEXT,
        image TEXT,
        capacity INTEGER,
        price_per_hour REAL,
        status TEXT DEFAULT 'Available',
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT NOT NULL,
        table_name TEXT NOT NULL,
        record_id INTEGER,
        description TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

init_db()


# ======================
# HELPERS
# ======================
def render_with_active(template, active_page):
    return render_template(template, active_page=active_page)


# ======================
# ROUTES
# ======================
@app.route('/')
def index():
    user_data = None

    if 'user' in session:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name, email, profile_image FROM users WHERE email=?",
            (session['user'],)
        )
        user_data = cursor.fetchone()
        conn.close()

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM categories WHERE status='Available'")
    categories = cursor.fetchall()

    cursor.execute("SELECT * FROM facilities WHERE status='Available'")
    facilities_raw = cursor.fetchall()
    conn.close()

    facilities = []
    for f in facilities_raw:
        facility = dict(f)
        image_file = facility.get("image") or facility.get("facility_image")
        if image_file:
            facility["image_url"] = url_for('static', filename=f'uploads/facilities/{image_file}')
        else:
            facility["image_url"] = url_for('static', filename='uploads/facilities/default.png')
        facilities.append(facility)

    return render_template(
        "index.html",
        user=user_data,
        categories=categories,
        facilities=facilities,
    )


# ======================
# LOGIN
# ======================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        conn = None

        try:
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            action = request.form.get('action')

            # ======================
            # SIGNUP
            # ======================
            if action == 'signup':
                name             = request.form.get('name')
                email            = request.form.get('email')
                password         = request.form.get('password')
                confirm_password = request.form.get('confirm_password')

                if password != confirm_password:
                    return jsonify({"status": "error", "message": "Passwords do not match"})

                hashed_pw = generate_password_hash(password)

                cursor.execute(
                    "INSERT INTO users (name, email, password, status) VALUES (?, ?, ?, ?)",
                    (name, email, hashed_pw, "active")
                )
                conn.commit()

                email_service.send_email(
                    recipient_email=email,
                    subject="Welcome to Sports Complex Booking System",
                    message_html=build_email(
                        title="Welcome to Sports Complex!",
                        name=name,
                        body_html=f"""
                        <p style="color: #555; font-size: 14px; line-height: 1.6;">
                            Your account has been created successfully.
                            You can now log in to the Sports Complex Booking System.
                        </p>
                        <p style="color: #555; font-size: 14px; line-height: 1.6;">
                            <strong>Status:</strong>
                            <span style="color: #38a169; font-weight: 600;">Active</span>
                        </p>
                        <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">
                        <p style="color: #888; font-size: 12px; line-height: 1.6;">
                            If you did not create this account, please contact our support team immediately.
                        </p>
                        """
                    )
                )

                return jsonify({"status": "success", "message": "Account created successfully"})

            # ======================
            # LOGIN
            # ======================
            elif action == 'login':
                email    = request.form.get('email')
                password = request.form.get('password')

                cursor.execute("SELECT * FROM users WHERE email=?", (email,))
                user = cursor.fetchone()

                if not user:
                    return jsonify({"status": "error", "message": "Account not found"})

                name   = user['name']
                status = user['status'] if 'status' in user.keys() else 'active'

                if status == "inactive":
                    email_service.send_email(
                        recipient_email=email,
                        subject="Login Attempt Failed – Sports Complex",
                        message_html=build_email(
                            title="Login Attempt Failed",
                            name=name,
                            body_html="""
                            <p style="color: #555; font-size: 14px; line-height: 1.6;">
                                We detected a login attempt on your <strong>Sports Complex</strong>
                                account. However, your account is currently
                                <strong style="color: #f59e0b;">Inactive</strong>.
                            </p>
                            <p style="color: #555; font-size: 14px; line-height: 1.6;">
                                Please contact our support team to activate your account.
                            </p>
                            <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">
                            <p style="color: #888; font-size: 12px; line-height: 1.6;">
                                If you did not attempt to log in, please ignore this email.
                            </p>
                            """
                        )
                    )
                    return jsonify({"status": "error", "message": "This account is not active. Please contact support."})

                if status == "banned":
                    email_service.send_email(
                        recipient_email=email,
                        subject="Login Attempt Blocked – Sports Complex",
                        message_html=build_email(
                            title="Login Attempt Blocked",
                            name=name,
                            body_html="""
                            <p style="color: #555; font-size: 14px; line-height: 1.6;">
                                We detected a login attempt on your <strong>Sports Complex</strong>
                                account. However, your account has been
                                <strong style="color: #e53e3e;">Banned</strong>.
                            </p>
                            <p style="color: #555; font-size: 14px; line-height: 1.6;">
                                You are not allowed to access this system.
                                Please contact our support team for more information.
                            </p>
                            <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">
                            <p style="color: #888; font-size: 12px; line-height: 1.6;">
                                If you did not attempt to log in, please ignore this email.
                            </p>
                            """
                        )
                    )
                    return jsonify({"status": "error", "message": "Your account has been banned. Please contact support for more information."})

                if check_password_hash(user['password'], password):
                    session['user'] = user['email']

                    email_service.send_email(
                        recipient_email=email,
                        subject="Login Notification – Sports Complex",
                        message_html=build_email(
                            title="Login Notification",
                            name=name,
                            body_html="""
                            <p style="color: #555; font-size: 14px; line-height: 1.6;">
                                You have successfully logged in to your
                                <strong>Sports Complex</strong> account.
                                If you did not perform this action, please reset your password immediately.
                            </p>
                            <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">
                            <p style="color: #888; font-size: 12px; line-height: 1.6;">
                                If this was you, no further action is required.
                            </p>
                            """
                        )
                    )
                    return jsonify({"status": "success", "message": "Login successful"})

                return jsonify({"status": "error", "message": "Invalid credentials"})

        except Exception as e:
            print("LOGIN ERROR:", e)
            return jsonify({"status": "error", "message": str(e)})

        finally:
            if conn:
                conn.close()

    return render_template('auth/login.html')


@app.context_processor
def inject_user():
    if 'user' in session:
        try:
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name, email, profile_image FROM users WHERE email=?",
                (session['user'],)
            )
            user = cursor.fetchone()
            conn.close()
            if user:
                return dict(user=user)
        except Exception as e:
            print("USER FETCH ERROR:", e)
    return dict(user=None)


@app.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (session['user'],))
    user = cursor.fetchone()

    cursor.execute("SELECT id FROM users WHERE email = ?", (session['user'],))
    user_row = cursor.fetchone()
    uid = user_row['id']

    cursor.execute("SELECT COUNT(*) FROM reservations WHERE user_id = ?", (uid,))
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reservations WHERE user_id = ? AND status = 'Approved'", (uid,))
    approved = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reservations WHERE user_id = ? AND status = 'Pending'", (uid,))
    pending = cursor.fetchone()[0]

    conn.close()

    stats = {"total": total, "approved": approved, "pending": pending}
    return render_template("profile.html", user=user, stats=stats)


@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'user' not in session:
        return jsonify({"status": "error", "message": "Unauthorized. Please login again."}), 401

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        name    = request.form.get('name')
        phone   = request.form.get('phone')
        address = request.form.get('address')
        email   = session['user']

        cursor.execute("SELECT id FROM users WHERE email=?", (email,))
        user_row = cursor.fetchone()

        if not user_row:
            return jsonify({"status": "error", "message": "User not found"}), 404

        user_id            = user_row['id']
        profile_image_path = None
        file               = request.files.get('profile_image')

        if file and file.filename != "":
            filename      = secure_filename(file.filename)
            upload_folder = os.path.join('static', 'uploads', 'profiles')
            os.makedirs(upload_folder, exist_ok=True)
            filepath      = os.path.join(upload_folder, filename)
            file.save(filepath)
            profile_image_path = "/" + filepath.replace("\\", "/")

        if profile_image_path:
            cursor.execute("""
                UPDATE users SET name = ?, phone = ?, address = ?, profile_image = ? WHERE id = ?
            """, (name, phone, address, profile_image_path, user_id))
        else:
            cursor.execute("""
                UPDATE users SET name = ?, phone = ?, address = ? WHERE id = ?
            """, (name, phone, address, user_id))

        conn.commit()
        return jsonify({"status": "success", "message": "Profile updated successfully"})

    except Exception as e:
        print("UPDATE PROFILE ERROR:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        conn.close()


@app.route('/change_password', methods=['POST'])
def change_password():
    if 'user' not in session:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    current_pw  = request.form.get('current_password', '')
    new_pw      = request.form.get('new_password', '')
    confirm_pw  = request.form.get('confirm_password', '')

    if not current_pw or not new_pw or not confirm_pw:
        return jsonify({"status": "error", "message": "All fields are required."})

    if len(new_pw) < 6:
        return jsonify({"status": "error", "message": "Password must be at least 6 characters."})

    if new_pw != confirm_pw:
        return jsonify({"status": "error", "message": "New passwords do not match."})

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (session['user'],))
    user = cursor.fetchone()

    if not check_password_hash(user['password'], current_pw):
        conn.close()
        return jsonify({"status": "error", "message": "Current password is incorrect."})

    cursor.execute("UPDATE users SET password = ? WHERE email = ?",
                   (generate_password_hash(new_pw), session['user']))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})


# ======================
# ADMIN PAGES
# ======================
@app.route('/admin', methods=['GET', 'POST'])
def dashboard():

    if request.method == 'POST':
        email    = request.form.get('email')
        password = request.form.get('password')

        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND role = 'admin'", (email,))
        admin = cursor.fetchone()
        conn.close()

        if admin and check_password_hash(admin['password'], password):
            session['admin'] = admin['email']
            return redirect(url_for('dashboard'))

        return render_template('auth/admin-login.html', error="Invalid admin credentials")

    if 'admin' not in session:
        return render_template('auth/admin-login.html')

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM reservations")
    reservations_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM categories")
    categories_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM facilities")
    facilities_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM users")
    users_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM inquiries")
    inquiries_count = cursor.fetchone()[0]

    cursor.execute("SELECT IFNULL(SUM(total_amount), 0) FROM reservations WHERE status = 'Approved'")
    total_sales = cursor.fetchone()[0]

    cursor.execute("""
        SELECT
            r.id, r.booking_date, r.start_time, r.end_time, r.status,
            r.facility_id, r.user_id,
            u.name AS user_name,
            f.name AS facility_name
        FROM reservations r
        LEFT JOIN users u ON r.user_id = u.id
        LEFT JOIN facilities f ON r.facility_id = f.id
        WHERE r.status = 'Approved'
        ORDER BY r.id DESC
    """)

    active_rows         = cursor.fetchall()
    active_reservations = []

    for r in active_rows:
        row               = dict(r)
        row["end_datetime"] = f"{row['booking_date']} {row['end_time']}"
        active_reservations.append(row)

    conn.close()

    return render_template(
        'admin/dashboard.html',
        active_page='dashboard',
        reservations_count=reservations_count,
        categories_count=categories_count,
        facilities_count=facilities_count,
        users_count=users_count,
        inquiries_count=inquiries_count,
        total_sales=total_sales,
        active_reservations=active_reservations
    )


@app.route('/reservations')
def reservations():
    return render_with_active('admin/reservations.html', 'reservations')

@app.route('/get_booked_slots')
def get_booked_slots():
    facility_id = request.args.get('facility_id')
    date        = request.args.get('date')

    if not facility_id or not date:
        return jsonify({'booked_slots': []})

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT start_time, end_time
        FROM reservations
        WHERE facility_id = ?
          AND booking_date = ?
          AND status IN ('Pending', 'Approved')
    """, (facility_id, date))

    rows  = cursor.fetchall()
    conn.close()

    slots = []
    for row in rows:
        try:
            start_dt = datetime.strptime(row['start_time'], "%I:%M %p")
            end_dt   = datetime.strptime(row['end_time'],   "%I:%M %p")
            slots.append({
                'start_hour': start_dt.hour,
                'end_hour':   end_dt.hour
            })
        except Exception as e:
            print("Slot parse error:", e)

    return jsonify({'booked_slots': slots})

@app.route('/categories')
def categories():
    return render_with_active('admin/categories.html', 'categories')

@app.route('/facilities')
def facilities():
    return render_with_active('admin/facilities.html', 'facilities')

@app.route('/users')
def users():
    return render_with_active('admin/users.html', 'users')


# ======================
# INQUIRIES
# ======================
@app.route('/inquiries')
def inquiries():
    cursor.execute("SELECT * FROM inquiries")
    data = cursor.fetchall()
    return render_template('admin/inquiries.html', inquiries=data, active_page='inquiries')

@app.route('/delete_inquiry/<int:id>')
def delete_inquiry(id):
    cursor.execute("DELETE FROM inquiries WHERE id = ?", (id,))
    conn.commit()
    return redirect(url_for('inquiries'))

@app.route('/update_inquiry/<int:id>', methods=['POST'])
def update_inquiry(id):
    data = request.get_json()
    cursor.execute("""
        UPDATE inquiries SET name=?, email=?, message=? WHERE id=?
    """, (data['name'], data['email'], data['message'], id))
    conn.commit()
    return jsonify({"status": "success"})


# ======================
# HISTORY LOG
# ======================
@app.route('/history_log')
def history_log():
    cursor.execute("SELECT * FROM history_log ORDER BY created_at ASC")
    logs = cursor.fetchall()
    return render_template('admin/history-log.html', history_logs=logs, active_page='history_log')


# ======================
# OTHER PAGES
# ======================
@app.route('/transaction_log')
def transaction_log():
    return render_with_active('admin/transaction-log.html', 'transaction_log')

@app.route('/settings')
def settings():
    return render_with_active('admin/settings.html', 'settings')


@app.route('/my_bookings')
def my_bookings():
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE email = ?", (session['user'],))
    user_row = cursor.fetchone()

    cursor.execute("""
        SELECT r.*, f.name AS facility_name
        FROM reservations r
        LEFT JOIN facilities f ON r.facility_id = f.id
        WHERE r.user_id = ?
        ORDER BY r.date_created DESC
    """, (user_row['id'],))

    bookings = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return render_template('my_bookings.html', bookings=bookings)


@app.route('/cancel_booking/<int:id>', methods=['POST'])
def cancel_booking(id):
    if 'user' not in session:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE email = ?", (session['user'],))
    user_row = cursor.fetchone()

    cursor.execute("""
        UPDATE reservations SET status = 'Cancelled'
        WHERE id = ? AND user_id = ? AND status = 'Pending'
    """, (id, user_row['id']))

    conn.commit()
    affected = cursor.rowcount
    conn.close()

    if affected == 0:
        return jsonify({"status": "error", "message": "Booking not found or cannot be cancelled."})

    return jsonify({"status": "success"})


# ======================
# CONTACT
# ======================
@app.route('/contact', methods=['POST'])
def contact():
    data    = request.get_json()
    name    = data.get('name')
    email   = data.get('email')
    message = data.get('message')

    cursor.execute(
        "INSERT INTO inquiries (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )
    conn.commit()
    return jsonify({"status": "success"})


# ======================
# EXTEND RESERVATION
# ======================
@app.route("/extend_reservation", methods=["POST"])
def extend_reservation():
    try:
        data           = request.get_json()
        reservation_id = data.get("reservation_id")
        minutes        = data.get("minutes")

        if minutes == "30 mins":
            add_time = 30
        elif minutes == "1 hour":
            add_time = 60
        else:
            return jsonify({"status": "error", "message": "Invalid duration"}), 400

        conn = sqlite3.connect("database.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT booking_date, end_time FROM reservations WHERE id = ?", (reservation_id,))
        row = cursor.fetchone()

        if not row:
            return jsonify({"status": "error", "message": "Reservation not found"}), 404

        try:
            current_end_str = f"{row['booking_date']} {row['end_time']}"
            current_end     = datetime.strptime(current_end_str, "%B %d, %Y %I:%M %p")
        except Exception:
            return jsonify({"status": "error", "message": "Invalid date format in database"}), 500

        new_end          = current_end + timedelta(minutes=add_time)
        new_end_time     = new_end.strftime("%I:%M %p")
        new_booking_date = new_end.strftime("%B %d, %Y")

        cursor.execute("""
            UPDATE reservations
            SET end_time = ?, booking_date = ?, date_updated = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (new_end_time, new_booking_date, reservation_id))

        conn.commit()
        conn.close()

        return jsonify({
            "status": "success",
            "message": "Reservation extended successfully",
            "new_end_time": new_end_time,
            "new_date": new_booking_date
        })

    except sqlite3.OperationalError as e:
        return jsonify({"status": "error", "message": f"Database error: {str(e)}"}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# ======================
# LOGOUT
# ======================
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# ======================
# RUN APP
# ======================
if __name__ == '__main__':
    app.run(debug=True)