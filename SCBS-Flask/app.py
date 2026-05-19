import os
import re
import sqlite3
from flask import Flask, render_template, redirect, url_for, session, request, jsonify
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

from fetch_users import fetch_user
from fetch_inquiries import fetch_inquiry
from fetch_categories import fetch_categories
from fetch_facility import fetch_facility
from fetch_reservations import fetch_reservations
from create_reservation import create_reservation
from chatbot import chatbot
from email_notifications import EmailNotification

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
# DATABASE CONNECTION
# ======================
db_path = os.path.join(BASE_DIR, 'database.db')
conn = sqlite3.connect(db_path, check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()



email_service = EmailNotification(
    sender_email="arturoyparraguirre01@gmail.com",
    sender_password="zhuc cwnd vdhu nqmg"
)

# ======================
# CREATE TABLES
# ======================
def init_db():



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        -- 🔗 RELATIONSHIPS
        facility_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,

        -- 📅 SCHEDULE
        booking_date TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,

        -- 💰 PAYMENT INFO
        total_amount REAL NOT NULL,
        deposit_amount REAL NOT NULL,
        payment_method TEXT DEFAULT 'GCash',

        gcash_reference TEXT,
        payment_screenshot TEXT,  -- filename/path

        -- 📊 STATUS FLOW
        status TEXT DEFAULT 'Pending',  
        -- Pending / Approved / Rejected / Cancelled

        -- 📝 OPTIONAL INFO
        purpose TEXT,

        -- ⏱ TIMESTAMPS
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        date_updated TIMESTAMP,

        -- 🔗 FOREIGN KEYS (optional but recommended)
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
        role TEXT DEFAULT 'user',              -- admin / user
        status TEXT DEFAULT 'active',          -- active / inactive / banned
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        profile_image TEXT                    -- optional (path or URL)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL,

        status TEXT DEFAULT 'unread',         -- unread / read

        remarks TEXT,                         -- admin notes / decision (Approved, Declined, etc.)

        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME                  -- updated when admin edits remarks
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

    # ======================
    # FACILITIES TABLE (UPDATED)
    # ======================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS facilities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        category_id INTEGER NOT NULL,  -- 🔗 FK to categories
        name TEXT NOT NULL,
        description TEXT,
        image TEXT,                    -- 📷 store filename or path
        capacity INTEGER,              -- 👥 max number of users
        price_per_hour REAL,           -- 💰 optional pricing
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

    # ======================
    # USER SESSION
    # ======================
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

    # ======================
    # CATEGORIES
    # ======================
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM categories WHERE status='Available'")
    categories = cursor.fetchall()

    # ======================
    # FACILITIES (WITH IMAGE PATH FIX)
    # ======================
    cursor.execute("SELECT * FROM facilities WHERE status='Available'")
    facilities_raw = cursor.fetchall()
    conn.close()

    facilities = []
    for f in facilities_raw:
        facility = dict(f)

        # assumes your DB column is: image or facility_image
        image_file = facility.get("image") or facility.get("facility_image")

        if image_file:
            facility["image_url"] = url_for(
                'static',
                filename=f'uploads/facilities/{image_file}'
            )
        else:
            facility["image_url"] = url_for(
                'static',
                filename='uploads/facilities/default.png'
            )

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
                name = request.form.get('name')
                email = request.form.get('email')
                password = request.form.get('password')
                confirm_password = request.form.get('confirm_password')

                if password != confirm_password:
                    return jsonify({"status": "error", "message": "Passwords do not match"})

                hashed_pw = generate_password_hash(password)

                cursor.execute(
                    "INSERT INTO users (name, email, password, status) VALUES (?, ?, ?, ?)",
                    (name, email, hashed_pw, "active")
                )

                conn.commit()

                # ======================
                # EMAIL: SIGNUP SUCCESS
                # ======================
                email_service.send_email(
                    recipient_email=email,
                    subject="Welcome to Sports Complex Booking System",
                    message_html=f"""
                        <h2>Welcome {name}!</h2>
                        <p>Your account has been created successfully.</p>
                        <p>Status: <b>Inactive</b></p>
                        <p>Please wait for admin approval before you can log in.</p>
                    """
                )

                return jsonify({"status": "success", "message": "Account created successfully"})

            # ======================
            # LOGIN
            # ======================
            elif action == 'login':
                email = request.form.get('email')
                password = request.form.get('password')

                cursor.execute(
                    "SELECT * FROM users WHERE email=?",
                    (email,)
                )

                user = cursor.fetchone()

                if not user:
                    return jsonify({
                        "status": "error",
                        "message": "Account not found"
                    })

                name = user['name']

                # ======================
                # CHECK ACCOUNT STATUS
                # ======================
                status = user['status'] if 'status' in user.keys() else 'active'

                if status == "inactive":

                    email_service.send_email(
                        recipient_email=email,
                        subject="Login Attempt Failed - Inactive Account",
                        message_html=f"""
                            <h3>Hello {name},</h3>
                            <p>We detected a login attempt on your account.</p>
                            <p><b>Status:</b> Inactive</p>
                            <p>Please contact support to activate your account.</p>
                        """
                    )

                    return jsonify({
                        "status": "error",
                        "message": "Your account is not activated yet."
                    })

                if status == "banned":

                    email_service.send_email(
                        recipient_email=email,
                        subject="Login Attempt Blocked - Banned Account",
                        message_html=f"""
                            <h3>Hello {name},</h3>
                            <p>We detected a login attempt on your account.</p>
                            <p><b>Status:</b> Banned</p>
                            <p>You are not allowed to access this system.</p>
                        """
                    )

                    return jsonify({
                        "status": "error",
                        "message": "Your account has been banned. Please contact support for more information."
                    })

                # ======================
                # PASSWORD CHECK
                # ======================
                if check_password_hash(user['password'], password):

                    session['user'] = user['email']

                    # EMAIL: LOGIN SUCCESS
                    email_service.send_email(
                        recipient_email=email,
                        subject="Login Notification",
                        message_html=f"""
                            <h3>Hello {name},</h3>
                            <p>You have successfully logged in to your account.</p>
                        """
                    )

                    return jsonify({
                        "status": "success",
                        "message": "Login successful"
                    })

                return jsonify({
                    "status": "error",
                    "message": "Invalid credentials"
                })

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
                return dict(user=user)  # ✅ Now user is a full object

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

    cursor.execute("""
        SELECT * FROM users WHERE email = ?
    """, (session['user'],))

    user = cursor.fetchone()

    conn.close()

    return render_template("profile.html", user=user)


@app.route('/update_profile', methods=['POST'])
def update_profile():

    if 'user' not in session:
        return jsonify({
            "status": "error",
            "message": "Unauthorized. Please login again."
        }), 401

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')

        # Get email from session
        email = session['user']

        # Get user_id from database using email
        cursor.execute("SELECT id FROM users WHERE email=?", (email,))
        user_row = cursor.fetchone()

        if not user_row:
            return jsonify({
                "status": "error",
                "message": "User not found"
            }), 404

        user_id = user_row['id']

        profile_image_path = None

        file = request.files.get('profile_image')

        if file and file.filename != "":
            filename = secure_filename(file.filename)

            upload_folder = os.path.join('static', 'uploads', 'profiles')
            os.makedirs(upload_folder, exist_ok=True)

            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)

            profile_image_path = "/" + filepath.replace("\\", "/")

        if profile_image_path:
            cursor.execute("""
                UPDATE users
                SET name = ?, phone = ?, address = ?, profile_image = ?
                WHERE id = ?
            """, (name, phone, address, profile_image_path, user_id))
        else:
            cursor.execute("""
                UPDATE users
                SET name = ?, phone = ?, address = ?
                WHERE id = ?
            """, (name, phone, address, user_id))

        conn.commit()

        return jsonify({
            "status": "success",
            "message": "Profile updated successfully"
        })

    except Exception as e:
        print("UPDATE PROFILE ERROR:", e)

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

    finally:
        conn.close()
# ======================
# ADMIN PAGES
# ======================
# ======================
# ADMIN LOGIN
# ======================
@app.route('/admin', methods=['GET', 'POST'])
def dashboard():

    # ======================
    # ADMIN LOGIN PROCESS
    # ======================
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM users
            WHERE email = ? AND role = 'admin'
        """, (email,))

        admin = cursor.fetchone()

        conn.close()

        # ======================
        # CHECK ADMIN ACCOUNT
        # ======================
        if admin and check_password_hash(admin['password'], password):

            session['admin'] = admin['email']

            return redirect(url_for('dashboard'))

        return render_template(
            'auth/admin-login.html',
            error="Invalid admin credentials"
        )

    # ======================
    # CHECK ADMIN SESSION
    # ======================
    if 'admin' not in session:
        return render_template('auth/admin-login.html')

    # ======================
    # DASHBOARD DATA
    # ======================
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # ======================
    # COUNTS
    # ======================
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

    # ======================
    # SALES
    # ======================
    cursor.execute("""
        SELECT IFNULL(SUM(total_amount), 0)
        FROM reservations
        WHERE status = 'Approved'
    """)
    total_sales = cursor.fetchone()[0]

    # ======================
    # ACTIVE RESERVATIONS
    # ======================
    cursor.execute("""
        SELECT
            r.id,
            r.booking_date,
            r.start_time,
            r.end_time,
            r.status,

            r.facility_id,
            r.user_id,

            u.name AS user_name,
            f.name AS facility_name

        FROM reservations r

        LEFT JOIN users u ON r.user_id = u.id
        LEFT JOIN facilities f ON r.facility_id = f.id

        WHERE r.status = 'Approved'
        ORDER BY r.id DESC
    """)

    active_rows = cursor.fetchall()

    active_reservations = []

    for r in active_rows:
        row = dict(r)

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

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # ======================
    # COUNTS
    # ======================
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

    # ======================
    # SALES (APPROVED ONLY)
    # ======================
    cursor.execute("""
        SELECT IFNULL(SUM(total_amount), 0)
        FROM reservations
        WHERE status = 'Approved'
    """)
    total_sales = cursor.fetchone()[0]

    # ======================
    # ACTIVE / ONGOING RESERVATIONS
    # (APPROVED ONLY FOR LIVE MONITORING)
    # ======================
    cursor.execute("""
        SELECT
            r.id,
            r.booking_date,
            r.start_time,
            r.end_time,
            r.status,

            r.facility_id,
            r.user_id,

            u.name AS user_name,
            f.name AS facility_name

        FROM reservations r

        LEFT JOIN users u ON r.user_id = u.id
        LEFT JOIN facilities f ON r.facility_id = f.id

        WHERE r.status = 'Approved'
        ORDER BY r.id DESC
    """)

    active_rows = cursor.fetchall()

    active_reservations = []

    for r in active_rows:
        row = dict(r)

        # Convert to datetime format for JS countdown
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

        # 🔥 LIVE MONITORING DATA
        active_reservations=active_reservations
    )

    
@app.route('/reservations')
def reservations():
    return render_with_active('admin/reservations.html', 'reservations')

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
        UPDATE inquiries 
        SET name=?, email=?, message=? 
        WHERE id=?
    """, (data['name'], data['email'], data['message'], id))

    conn.commit()
    return jsonify({"status": "success"})

# ======================
# HISTORY LOG (IMPORTANT FIX HERE)
# ======================
@app.route('/history_log')
def history_log():
    cursor.execute("SELECT * FROM history_log ORDER BY created_at ASC")
    logs = cursor.fetchall()

    return render_template(
        'admin/history-log.html',
        history_logs=logs,
        active_page='history_log'
    )

# ======================
# OTHER PAGES
# ======================
@app.route('/transaction_log')
def transaction_log():
    return render_with_active('admin/transaction-log.html', 'transaction_log')

@app.route('/settings')
def settings():
    return render_with_active('admin/settings.html', 'settings')

# ======================
# CONTACT
# ======================
@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    cursor.execute(
        "INSERT INTO inquiries (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )
    conn.commit()

    return jsonify({"status": "success"})



@app.route("/extend_reservation", methods=["POST"])
def extend_reservation():
    try:
        data = request.get_json()
        reservation_id = data.get("reservation_id")
        minutes = data.get("minutes")

        # ------------------------
        # Convert dropdown value
        # ------------------------
        if minutes == "30 mins":
            add_time = 30
        elif minutes == "1 hour":
            add_time = 60
        else:
            return jsonify({"status": "error", "message": "Invalid duration"}), 400

        conn = sqlite3.connect("database.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # ------------------------
        # Get reservation
        # ------------------------
        cursor.execute("""
            SELECT booking_date, end_time
            FROM reservations
            WHERE id = ?
        """, (reservation_id,))

        row = cursor.fetchone()

        if not row:
            return jsonify({"status": "error", "message": "Reservation not found"}), 404

        # ------------------------
        # Parse time safely
        # ------------------------
        try:
            current_end_str = f"{row['booking_date']} {row['end_time']}"
            
            # Example expected format:
            # "May 19, 2026 10:00 AM"
            current_end = datetime.strptime(current_end_str, "%B %d, %Y %I:%M %p")

        except Exception:
            return jsonify({
                "status": "error",
                "message": "Invalid date format in database"
            }), 500

        # ------------------------
        # Add time
        # ------------------------
        new_end = current_end + timedelta(minutes=add_time)

        new_end_time = new_end.strftime("%I:%M %p")  # store only time
        new_booking_date = new_end.strftime("%B %d, %Y")

        # ------------------------
        # Update DB
        # ------------------------
        cursor.execute("""
            UPDATE reservations
            SET end_time = ?,
                booking_date = ?,
                date_updated = CURRENT_TIMESTAMP
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
        return jsonify({
            "status": "error",
            "message": f"Database error: {str(e)}"
        }), 500

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


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