from flask import Blueprint, request, jsonify, session
import sqlite3
import os
from werkzeug.utils import secure_filename
from email_notifications import EmailNotification

# ======================
# BLUEPRINT
# ======================
create_reservation = Blueprint('create_reservation', __name__)

# ======================
# DATABASE
# ======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, 'database.db')

# ======================
# UPLOAD FOLDER
# ======================
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads', 'payments')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ======================
# EMAIL SERVICE
# ======================
email_service = EmailNotification(
    sender_email="sportscomplexx1@gmail.com",
    sender_password="kaiu ouav fgqv kfsa"
)


# ======================
# CREATE RESERVATION
# ======================
@create_reservation.route('/create_reservation', methods=['POST'])
def create_new_reservation():

    try:

        # ── Auth check ──────────────────────────────────
        if 'user' not in session:
            return jsonify({"status": "error", "message": "Please login first"})

        # ── DB connection ────────────────────────────────
        conn   = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # ── Get user ─────────────────────────────────────
        cursor.execute("SELECT id, name, email FROM users WHERE email=?", (session['user'],))
        user = cursor.fetchone()

        if not user:
            conn.close()
            return jsonify({"status": "error", "message": "User not found"})

        user_id    = user['id']
        user_name  = user['name']
        user_email = user['email']

        # ── Form data ─────────────────────────────────────
        facility_id     = request.form.get('facility_id')
        booking_date    = request.form.get('booking_date')
        start_time      = request.form.get('start_time')
        end_time        = request.form.get('end_time')
        total_amount    = request.form.get('total_amount')
        deposit_amount  = request.form.get('deposit_amount')
        purpose         = request.form.get('purpose') or '—'
        gcash_reference = request.form.get('gcash_reference')

        # ── Facility name (for email) ─────────────────────
        cursor.execute("SELECT name FROM facilities WHERE id = ?", (facility_id,))
        facility_row  = cursor.fetchone()
        facility_name = facility_row['name'] if facility_row else f"Facility #{facility_id}"

        # ── Screenshot upload ─────────────────────────────
        screenshot          = request.files.get('payment_screenshot')
        screenshot_filename = None

        if screenshot:
            filename            = secure_filename(screenshot.filename)
            screenshot_filename = f"{gcash_reference}_{filename}"
            screenshot.save(os.path.join(UPLOAD_FOLDER, screenshot_filename))

        # ── Insert reservation ────────────────────────────
        cursor.execute("""
            INSERT INTO reservations (
                facility_id, user_id,
                booking_date, start_time, end_time,
                total_amount, deposit_amount,
                payment_method,
                gcash_reference, payment_screenshot,
                status, purpose
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            facility_id, user_id,
            booking_date, start_time, end_time,
            total_amount, deposit_amount,
            'GCash',
            gcash_reference, screenshot_filename,
            'Pending', purpose
        ))

        conn.commit()
        conn.close()

        # ── Send email notification ───────────────────────
        try:
            # Format deposit to 2 decimal places
            deposit_fmt = f"₱{float(deposit_amount):,.2f}"
            total_fmt   = f"₱{float(total_amount):,.2f}"

            html_body = f"""
            <div style="font-family: 'Poppins', Arial, sans-serif; max-width: 520px;
                        margin: 0 auto; padding: 30px; border-radius: 12px;
                        border: 1px solid #e0e0e0; background: #ffffff;">

                <h2 style="color: #205072; margin-bottom: 8px;">Booking Submitted</h2>

                <p style="color: #555; font-size: 14px; line-height: 1.6;">
                    Hi <strong>{user_name}</strong>,
                </p>

                <p style="color: #555; font-size: 14px; line-height: 1.6;">
                    Your reservation has been submitted and is currently
                    <strong style="color: #f59e0b;">pending admin approval</strong>.
                    You will receive another email once your booking is confirmed.
                </p>

                <!-- Booking Details Card -->
                <div style="background: #f8fafc; border: 1px solid #e2e8f0;
                            border-radius: 10px; padding: 20px; margin: 24px 0;">

                    <p style="margin: 0 0 12px; font-size: 13px; font-weight: 700;
                               color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px;">
                        Booking Details
                    </p>

                    <table style="width: 100%; border-collapse: collapse; font-size: 14px; color: #555;">
                        <tr>
                            <td style="padding: 6px 0; color: #94a3b8; width: 40%;">Facility</td>
                            <td style="padding: 6px 0; font-weight: 600; color: #0f172a;">{facility_name}</td>
                        </tr>
                        <tr>
                            <td style="padding: 6px 0; color: #94a3b8;">Date</td>
                            <td style="padding: 6px 0; font-weight: 600; color: #0f172a;">{booking_date}</td>
                        </tr>
                        <tr>
                            <td style="padding: 6px 0; color: #94a3b8;">Time</td>
                            <td style="padding: 6px 0; font-weight: 600; color: #0f172a;">{start_time} – {end_time}</td>
                        </tr>
                        <tr>
                            <td style="padding: 6px 0; color: #94a3b8;">Purpose</td>
                            <td style="padding: 6px 0; font-weight: 600; color: #0f172a;">{purpose}</td>
                        </tr>
                        <tr>
                            <td style="padding: 6px 0; color: #94a3b8;">Payment</td>
                            <td style="padding: 6px 0; font-weight: 600; color: #0f172a;">GCash</td>
                        </tr>
                        <tr>
                            <td style="padding: 6px 0; color: #94a3b8;">GCash Ref #</td>
                            <td style="padding: 6px 0; font-weight: 600; color: #0f172a;">{gcash_reference}</td>
                        </tr>
                    </table>

                    <!-- Divider -->
                    <hr style="border: none; border-top: 1px dashed #e2e8f0; margin: 14px 0;">

                    <!-- Amount Summary -->
                    <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                        <tr>
                            <td style="padding: 5px 0; color: #555;">Total Amount</td>
                            <td style="padding: 5px 0; text-align: right;
                                       font-weight: 700; color: #0f172a;">{total_fmt}</td>
                        </tr>
                        <tr>
                            <td style="padding: 5px 0; color: #555;">Deposit Paid (30%)</td>
                            <td style="padding: 5px 0; text-align: right;
                                       font-weight: 700; color: #329D9C;">{deposit_fmt}</td>
                        </tr>
                    </table>
                </div>

                <!-- Status Badge -->
                <div style="text-align: center; margin: 20px 0;">
                    <span style="display: inline-block; background: #fef9c3; color: #92400e;
                                 padding: 8px 22px; border-radius: 999px;
                                 font-size: 13px; font-weight: 700; letter-spacing: 0.3px;">
                        ⏳ Pending Approval
                    </span>
                </div>

                <p style="color: #888; font-size: 12px; line-height: 1.6;">
                    If you did not make this booking or believe this is a mistake,
                    please contact our support team immediately.
                </p>

                <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">

                <p style="color: #aaa; font-size: 11px; text-align: center;">
                    © 2026 Sports Complex Booking System
                </p>
            </div>
            """

            email_service.send_email(
                recipient_email=user_email,
                subject="Booking Submitted – Sports Complex",
                message_html=html_body
            )

        except Exception as mail_err:
            # Email failure should never block the booking response
            print("EMAIL NOTIFICATION ERROR:", mail_err)

        return jsonify({"status": "success", "message": "Reservation created successfully"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})