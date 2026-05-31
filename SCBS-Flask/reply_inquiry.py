import os
import sqlite3
from flask import Blueprint, request, jsonify
from email_notifications import EmailNotification

# ── Config ───────────────────────────────────────────────────────────────────
SENDER_EMAIL    = "sportscomplexx1@gmail.com"
SENDER_PASSWORD = "kaiu ouav fgqv kfsa"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, "database.db")
# ─────────────────────────────────────────────────────────────────────────────

# IMPORTANT: blueprint name is 'inquiry_actions' — does NOT clash with
# the 'inquiries' endpoint defined in app.py.
inquiry_actions = Blueprint('inquiry_actions', __name__)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def build_reply_email(name, message):
    return f"""
    <div style="font-family: 'Poppins', Arial, sans-serif; max-width: 520px;
                margin: 0 auto; padding: 30px; border-radius: 12px;
                border: 1px solid #e0e0e0; background: #ffffff;">

        <h2 style="color: #205072; margin-bottom: 8px;">Response to Your Inquiry</h2>

        <p style="color: #555; font-size: 14px; line-height: 1.6;">
            Hi <strong>{name}</strong>,
        </p>

        <p style="color: #555; font-size: 14px; line-height: 1.6;">
            Thank you for reaching out to us. Here is our response to your inquiry:
        </p>

        <div style="background: #f9f9f9; border-left: 4px solid #329D9C;
                    padding: 14px 18px; border-radius: 0 8px 8px 0; margin: 20px 0;">
            <p style="color: #444; font-size: 14px; line-height: 1.7; margin: 0;
                      white-space: pre-wrap;">{message}</p>
        </div>

        <p style="color: #888; font-size: 12px; line-height: 1.6;">
            If you have further questions, feel free to reply to this email or contact us at
            <a href="mailto:{SENDER_EMAIL}" style="color: #329D9C;">{SENDER_EMAIL}</a>.
        </p>

        <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">

        <p style="color: #aaa; font-size: 11px; text-align: center;">
            © 2026 Sports Complex Booking System
        </p>
    </div>
    """


# GET /get_inquiry/<id>
@inquiry_actions.route('/get_inquiry/<int:inquiry_id>')
def get_inquiry(inquiry_id):
    try:
        conn = get_db()
        row  = conn.execute("SELECT * FROM inquiries WHERE id = ?", (inquiry_id,)).fetchone()
        conn.close()

        if not row:
            return jsonify({"status": "error", "message": "Inquiry not found."}), 404

        return jsonify({
            "id":         row["id"],
            "name":       row["name"],
            "email":      row["email"],
            "message":    row["message"],
            "remarks":    row["remarks"] or "",
            "status":     row["status"],
            "created_at": row["created_at"] or "—",
        })

    except Exception as e:
        print("GET INQUIRY ERROR:", e)
        return jsonify({"status": "error", "message": str(e)}), 500


# POST /mark_inquiry_read/<id>
@inquiry_actions.route('/mark_inquiry_read/<int:inquiry_id>', methods=['POST'])
def mark_inquiry_read(inquiry_id):
    try:
        conn = get_db()
        conn.execute("""
            UPDATE inquiries
            SET status = 'read', updated_at = CURRENT_TIMESTAMP
            WHERE id = ? AND status = 'unread'
        """, (inquiry_id,))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"})

    except Exception as e:
        print("MARK READ ERROR:", e)
        return jsonify({"status": "error", "message": str(e)}), 500


# POST /save_inquiry_remarks/<id>  (replaces update_inquiry to avoid name clash)
@inquiry_actions.route('/save_inquiry_remarks/<int:inquiry_id>', methods=['POST'])
def save_inquiry_remarks(inquiry_id):
    try:
        data    = request.get_json()
        remarks = (data.get("remarks") or "").strip()

        conn = get_db()
        conn.execute("""
            UPDATE inquiries
            SET remarks = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (remarks, inquiry_id))
        conn.commit()
        conn.close()

        return jsonify({"status": "success", "message": "Remarks saved."})

    except Exception as e:
        print("SAVE REMARKS ERROR:", e)
        return jsonify({"status": "error", "message": str(e)}), 500


# POST /remove_inquiry/<id>  (replaces delete_inquiry to avoid name clash)
@inquiry_actions.route('/remove_inquiry/<int:inquiry_id>', methods=['POST'])
def remove_inquiry(inquiry_id):
    try:
        conn = get_db()
        conn.execute("DELETE FROM inquiries WHERE id = ?", (inquiry_id,))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Inquiry deleted."})

    except Exception as e:
        print("DELETE INQUIRY ERROR:", e)
        return jsonify({"status": "error", "message": str(e)}), 500


# POST /reply_inquiry/<id>
@inquiry_actions.route('/reply_inquiry/<int:inquiry_id>', methods=['POST'])
def reply_to_inquiry(inquiry_id):
    try:
        data    = request.get_json()
        subject = (data.get("subject") or "Re: Your Inquiry – Sports Complex Booking System").strip()
        message = (data.get("message") or "").strip()

        if not message:
            return jsonify({"success": False, "message": "Reply message cannot be empty."}), 400

        conn    = get_db()
        inquiry = conn.execute("SELECT * FROM inquiries WHERE id = ?", (inquiry_id,)).fetchone()

        if not inquiry:
            conn.close()
            return jsonify({"success": False, "message": "Inquiry not found."}), 404

        notifier = EmailNotification(SENDER_EMAIL, SENDER_PASSWORD)
        sent = notifier.send_email(
            recipient_email=inquiry["email"],
            subject=subject,
            message_html=build_reply_email(inquiry["name"], message)
        )

        if not sent:
            conn.close()
            return jsonify({"success": False, "message": "Failed to send email. Please try again."}), 500

        conn.execute("""
            UPDATE inquiries
            SET status     = 'replied',
                remarks    = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (message, inquiry_id))
        conn.commit()
        conn.close()

        return jsonify({"success": True, "message": "Reply sent successfully."})

    except Exception as e:
        print("REPLY INQUIRY ERROR:", e)
        return jsonify({"success": False, "message": str(e)}), 500