import os
import secrets
import sqlite3
from datetime import datetime, timedelta
from flask import request, jsonify, render_template
from werkzeug.security import generate_password_hash

from email_notifications import EmailNotification


# ── Config ──────────────────────────────────────────────────────────────────
SENDER_EMAIL         = "arturoyparraguirre01@gmail.com"
SENDER_PASSWORD      = "zhuc cwnd vdhu nqmg"
TOKEN_EXPIRY_MINUTES = 30

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, "database.db")
# ───────────────────────────────────────────────────────────────────────────


def get_app_url():
    """
    Dynamically resolve the correct public base URL at request time.

    Priority:
      1. APP_URL env variable  (set this in production)
      2. CODESPACE_NAME env variable  (auto-set by GitHub Codespaces)
      3. X-Forwarded-Host / X-Forwarded-Proto headers  (reverse proxies)
      4. Flask request.host_url fallback
    """
    # 1. Explicit override (production / staging)
    explicit = os.environ.get("APP_URL", "").strip().rstrip("/")
    if explicit:
        return explicit

    # 2. GitHub Codespaces  →  https://<name>-5000.app.github.dev
    codespace = os.environ.get("CODESPACE_NAME", "").strip()
    if codespace:
        return f"https://{codespace}-5000.app.github.dev"

    # 3. Reverse-proxy headers (Ngrok, Railway, Render, etc.)
    forwarded_host  = request.headers.get("X-Forwarded-Host", "").strip()
    forwarded_proto = request.headers.get("X-Forwarded-Proto", "https").strip()
    if forwarded_host:
        return f"{forwarded_proto}://{forwarded_host}"

    # 4. Flask fallback  (works for plain localhost dev)
    return request.host_url.rstrip("/")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_reset_tokens_table():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS password_reset_tokens (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id    INTEGER NOT NULL,
            token      TEXT NOT NULL UNIQUE,
            expires_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)
    conn.commit()
    conn.close()


# ── /forgot-password  (POST) ────────────────────────────────────────────────
def forgot_password():
    email = (request.form.get("email") or "").strip().lower()

    if not email:
        return jsonify({"status": "error", "message": "Email is required."}), 400

    conn   = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, status FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    # Always return success to prevent email enumeration attacks
    if not user:
        conn.close()
        return jsonify({"status": "success"})

    if user["status"] in ("inactive", "banned"):
        conn.close()
        return jsonify({
            "status": "error",
            "message": "This account is not active. Please contact support."
        }), 403

    user_id   = user["id"]
    user_name = user["name"]

    # ── Generate token + expiry ─────────────────────────────────────────────
    token       = secrets.token_urlsafe(48)
    expires     = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRY_MINUTES)
    expires_str = expires.strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("DELETE FROM password_reset_tokens WHERE user_id = ?", (user_id,))
    cursor.execute(
        "INSERT INTO password_reset_tokens (user_id, token, expires_at) VALUES (?, ?, ?)",
        (user_id, token, expires_str)
    )
    conn.commit()
    conn.close()

    # ── Build reset link using dynamic base URL ─────────────────────────────
    base_url   = get_app_url()
    reset_link = f"{base_url}/reset-password?token={token}"

    print(f"[RESET LINK] {reset_link}")   # visible in terminal for debugging

    html_body = f"""
    <div style="font-family: 'Poppins', Arial, sans-serif; max-width: 520px;
                margin: 0 auto; padding: 30px; border-radius: 12px;
                border: 1px solid #e0e0e0; background: #ffffff;">

        <h2 style="color: #205072; margin-bottom: 8px;">Password Reset Request</h2>

        <p style="color: #555; font-size: 14px; line-height: 1.6;">
            Hi <strong>{user_name}</strong>,
        </p>

        <p style="color: #555; font-size: 14px; line-height: 1.6;">
            We received a request to reset the password for your
            <strong>Sports Complex</strong> account.
            Click the button below to set a new password.
            This link will expire in <strong>{TOKEN_EXPIRY_MINUTES} minutes</strong>.
        </p>

        <div style="text-align: center; margin: 30px 0;">
            <a href="{reset_link}"
               style="background: #329D9C; color: #ffffff; padding: 12px 32px;
                      border-radius: 8px; text-decoration: none;
                      font-size: 14px; font-weight: 600;">
                Reset My Password
            </a>
        </div>

        <p style="color: #888; font-size: 12px; line-height: 1.6;">
            If you did not request this, you can safely ignore this email —
            your password will remain unchanged.
        </p>

        <p style="color: #888; font-size: 12px; line-height: 1.6;">
            Or copy and paste this link into your browser:<br>
            <a href="{reset_link}" style="color: #329D9C;">{reset_link}</a>
        </p>

        <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">

        <p style="color: #aaa; font-size: 11px; text-align: center;">
            © 2026 Sports Complex Booking System
        </p>
    </div>
    """

    notifier = EmailNotification(SENDER_EMAIL, SENDER_PASSWORD)
    sent = notifier.send_email(
        recipient_email=email,
        subject="Reset Your Password – Sports Complex",
        message_html=html_body
    )

    if not sent:
        return jsonify({
            "status": "error",
            "message": "Failed to send reset email. Please try again later."
        }), 500

    return jsonify({"status": "success"})


# ── /reset-password  (GET + POST) ───────────────────────────────────────────
def reset_password():
    token = (request.args.get("token") or request.form.get("token") or "").strip()

    if request.method == "GET":
        if not token:
            return render_template("auth/reset_password.html", token="", error="Invalid or missing reset link.")
        return render_template("auth/reset_password.html", token=token, error=None)

    # POST
    new_password     = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")

    if not token:
        return jsonify({"status": "error", "message": "Reset token is missing."}), 400

    if len(new_password) < 6:
        return jsonify({"status": "error", "message": "Password must be at least 6 characters."}), 400

    if new_password != confirm_password:
        return jsonify({"status": "error", "message": "Passwords do not match."}), 400

    conn    = get_db()
    cursor  = conn.cursor()
    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "SELECT user_id FROM password_reset_tokens WHERE token = ? AND expires_at > ?",
        (token, now_str)
    )
    row = cursor.fetchone()

    if not row:
        conn.close()
        return jsonify({
            "status": "error",
            "message": "This reset link is invalid or has already expired. Please request a new one."
        }), 400

    user_id = row["user_id"]

    hashed_password = generate_password_hash(new_password)
    cursor.execute("UPDATE users SET password = ? WHERE id = ?", (hashed_password, user_id))
    cursor.execute("DELETE FROM password_reset_tokens WHERE token = ?", (token,))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})