import sqlite3
from werkzeug.security import generate_password_hash

# ======================
# DATABASE CONNECTION
# ======================
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# ======================
# ADMIN DETAILS
# ======================
name = "Administrator"
email = "admin@gmail.com"
password = "admin123"

# Hash password
hashed_password = generate_password_hash(password)

# ======================
# CHECK IF ADMIN EXISTS
# ======================
cursor.execute(
    "SELECT * FROM users WHERE email = ?",
    (email,)
)

existing_admin = cursor.fetchone()

if existing_admin:
    print("Admin account already exists.")
else:

    # ======================
    # INSERT ADMIN ACCOUNT
    # ======================
    cursor.execute("""
        INSERT INTO users (
            name,
            email,
            password,
            role,
            status
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        email,
        hashed_password,
        "admin",
        "active"
    ))

    conn.commit()

    print("Admin account inserted successfully.")
    print("Email: admin@gmail.com")
    print("Password: admin123")

# ======================
# CLOSE CONNECTION
# ======================
conn.close()