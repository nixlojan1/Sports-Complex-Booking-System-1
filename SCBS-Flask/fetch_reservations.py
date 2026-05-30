from flask import Blueprint, jsonify, request
import sqlite3
import os
from email_notifications import EmailNotification

# ======================
# Blueprint
# ======================
fetch_reservations = Blueprint('fetch_reservations', __name__)

# ======================
# DATABASE PATH
# ======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, 'database.db')

# ======================
# EMAIL SERVICE
# ======================
email_service = EmailNotification(
    sender_email    = "sportscomplexx1@gmail.com",
    sender_password = "kaiu ouav fgqv kfsa"
)

# ======================
# EMAIL TEMPLATES
# ======================
STATUS_CONFIG = {
    'Approved': {
        'subject'     : 'Booking Approved – Sports Complex',
        'badge_color' : '#059669',
        'badge_bg'    : '#d1fae5',
        'headline'    : 'Your Booking is Confirmed! 🎉',
        'intro'       : 'Great news! Your reservation has been <strong style="color:#059669;">approved</strong> by our team. Please review your booking details below.',
        'tip'         : 'Please arrive on time and bring a copy of this confirmation. Contact us if you need to make any changes.',
    },
    'Rejected': {
        'subject'     : 'Booking Not Approved – Sports Complex',
        'badge_color' : '#dc2626',
        'badge_bg'    : '#fee2e2',
        'headline'    : 'Booking Could Not Be Approved',
        'intro'       : 'We regret to inform you that your reservation has been <strong style="color:#dc2626;">rejected</strong>. You may submit a new booking for a different date or time slot.',
        'tip'         : 'Please contact us if you have any questions or need further assistance.',
    },
    'Cancelled': {
        'subject'     : 'Booking Cancelled – Sports Complex',
        'badge_color' : '#6b7280',
        'badge_bg'    : '#f3f4f6',
        'headline'    : 'Booking Cancelled',
        'intro'       : 'Your reservation has been <strong style="color:#6b7280;">cancelled</strong>. If you did not request this, please contact us immediately.',
        'tip'         : 'If a deposit was paid, please reach out to our team to discuss your refund.',
    },
    'Pending': {
        'subject'     : 'Booking Under Review – Sports Complex',
        'badge_color' : '#d97706',
        'badge_bg'    : '#fef3c7',
        'headline'    : 'Booking Is Under Review',
        'intro'       : 'Your reservation is currently <strong style="color:#d97706;">pending</strong> review by our team. We will notify you as soon as a decision has been made.',
        'tip'         : 'No action is required from you at this time. We appreciate your patience.',
    },
}


def build_status_email(user_name, status, r):
    """Build an HTML email body for a reservation status update."""

    cfg = STATUS_CONFIG.get(status, STATUS_CONFIG['Pending'])

    rows_html = ''.join([
        f"""<tr>
                <td style="padding:5px 0;color:#888;font-size:13px;">{label}</td>
                <td style="padding:5px 0;font-weight:600;font-size:13px;text-align:right;color:#1e293b;">{value}</td>
            </tr>"""
        for label, value in [
            ('Booking ID',    f"#{r['id']}"),
            ('Facility',      r['facility_name'] or 'N/A'),
            ('Date',          r['booking_date']),
            ('Time',          f"{r['start_time']} – {r['end_time']}"),
            ('Total Amount',  f"₱{float(r['total_amount'] or 0):,.2f}"),
            ('Deposit Paid',  f"₱{float(r['deposit_amount'] or 0):,.2f}"),
        ]
    ])

    return f"""
    <div style="font-family: 'Poppins', Arial, sans-serif; max-width: 520px;
                margin: 0 auto; padding: 30px; border-radius: 12px;
                border: 1px solid #e0e0e0; background: #ffffff;">

        <h2 style="color: #205072; margin-bottom: 8px;">{cfg['headline']}</h2>

        <p style="color: #555; font-size: 14px; line-height: 1.6;">
            Hi <strong>{user_name}</strong>,
        </p>

        <p style="color: #555; font-size: 14px; line-height: 1.6;">
            {cfg['intro']}
        </p>

        <!-- STATUS BADGE -->
        <div style="text-align: center; margin: 22px 0;">
            <span style="
                background: {cfg['badge_bg']};
                color: {cfg['badge_color']};
                padding: 10px 28px;
                border-radius: 999px;
                font-weight: 700;
                font-size: 15px;
                display: inline-block;
                letter-spacing: 0.5px;
            ">
                {status.upper()}
            </span>
        </div>

        <!-- BOOKING DETAILS -->
        <div style="background: #f8fafc; border-radius: 10px; padding: 18px; margin: 16px 0;
                    border: 1px solid #e2e8f0;">
            <h3 style="color: #205072; font-size: 13px; font-weight: 700;
                       text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 12px;">
                Booking Details
            </h3>
            <table style="width: 100%; border-collapse: collapse;">
                {rows_html}
            </table>
        </div>

        <!-- TIP BOX -->
        <div style="background: #fffbeb; border-left: 4px solid #f59e0b;
                    border-radius: 6px; padding: 12px 16px; margin: 16px 0;">
            <p style="color: #78350f; font-size: 13px; line-height: 1.6; margin: 0;">
                {cfg['tip']}
            </p>
        </div>

        <p style="color: #888; font-size: 12px; line-height: 1.6; margin-top: 16px;">
            For assistance, contact us at
            <a href="mailto:sportscomplexx1@gmail.com" style="color: #329D9C;">
                sportscomplexx1@gmail.com
            </a>
            or call <strong>+63 946 421 7995</strong>.
        </p>

        <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">

        <p style="color: #aaa; font-size: 11px; text-align: center;">
            © 2026 Sports Complex Booking System
        </p>
    </div>
    """


# ======================
# GET ALL RESERVATIONS
# ======================
@fetch_reservations.route('/get_reservations')
def get_reservations():

    conn   = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            r.id, r.facility_id, r.user_id,
            r.booking_date, r.start_time, r.end_time,
            r.total_amount, r.deposit_amount, r.payment_method,
            r.gcash_reference, r.payment_screenshot,
            r.status, r.purpose, r.date_created, r.date_updated,

            u.name  AS user_name,
            u.email AS user_email,
            u.phone AS user_phone,

            f.name          AS facility_name,
            f.price_per_hour,
            f.image         AS facility_image

        FROM reservations r
        LEFT JOIN users u ON r.user_id = u.id
        LEFT JOIN facilities f ON r.facility_id = f.id
        ORDER BY r.id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return jsonify([dict(row) for row in rows])


# ======================
# GET SINGLE RESERVATION
# ======================
@fetch_reservations.route('/get_reservation/<int:id>')
def get_reservation(id):

    conn   = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT r.*,
               u.name  AS user_name,
               u.email AS user_email,
               u.phone AS user_phone,
               f.name          AS facility_name,
               f.description   AS facility_description,
               f.image         AS facility_image,
               f.price_per_hour
        FROM reservations r
        LEFT JOIN users u ON r.user_id = u.id
        LEFT JOIN facilities f ON r.facility_id = f.id
        WHERE r.id = ?
    """, (id,))

    reservation = cursor.fetchone()
    conn.close()

    if reservation:
        return jsonify(dict(reservation))

    return jsonify({"status": "error", "message": "Reservation not found"})


# ======================
# UPDATE RESERVATION STATUS
# (sends email to customer)
# ======================
@fetch_reservations.route('/update_reservation_status/<int:id>', methods=['POST'])
def update_reservation_status(id):

    new_status = request.form.get('status')

    conn   = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # ── 1. Update the status ────────────────────────────
    cursor.execute("""
        UPDATE reservations
        SET status = ?, date_updated = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (new_status, id))
    conn.commit()

    # ── 2. Fetch full details for the email ─────────────
    cursor.execute("""
        SELECT r.id, r.booking_date, r.start_time, r.end_time,
               r.total_amount, r.deposit_amount,
               u.name AS user_name, u.email AS user_email,
               f.name AS facility_name
        FROM reservations r
        LEFT JOIN users u ON r.user_id = u.id
        LEFT JOIN facilities f ON r.facility_id = f.id
        WHERE r.id = ?
    """, (id,))

    reservation = cursor.fetchone()
    conn.close()

    # ── 3. Send notification email ───────────────────────
    if reservation and reservation['user_email']:
        try:
            email_service.send_email(
                recipient_email = reservation['user_email'],
                subject         = STATUS_CONFIG.get(new_status, STATUS_CONFIG['Pending'])['subject'],
                message_html    = build_status_email(
                    user_name  = reservation['user_name'] or 'Customer',
                    status     = new_status,
                    r          = dict(reservation)
                )
            )
        except Exception as e:
            print(f"[EMAIL ERROR] Failed to send status email: {e}")

    return jsonify({"status": "success", "message": "Reservation updated successfully"})


# ======================
# DELETE RESERVATION
# ======================
@fetch_reservations.route('/delete_reservation/<int:id>', methods=['POST'])
def delete_reservation(id):

    conn   = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM reservations WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "Reservation deleted successfully"})
