import sqlite3
import random
import re
from flask import Blueprint, request, jsonify, session

chatbot = Blueprint("chatbot", __name__)
DB_NAME = "database.db"


# ==========================
# DATABASE
# ==========================
def get_db():
    return sqlite3.connect(DB_NAME)


# ==========================
# HUMAN-LIKE RESPONSES
# ==========================
def humanize(text):
    prefixes = [
        "",
        "Got it. ",
        "Alright, ",
        "Sure thing! ",
        "No problem. ",
        "Here’s what I found: "
    ]
    return random.choice(prefixes) + text


# ==========================
# SMART INTENT SCORING
# ==========================
def detect_intents(message):
    msg = message.lower()

    intents = {
        "greeting": ["hi", "hello", "hey"],
        "categories": ["category", "categories", "type"],
        "facilities": ["facility", "court", "gym", "billiard"],
        "availability": ["available", "availability", "free"],
        "pricing": ["price", "cost", "rate"],
        "reservation": ["reserve", "book", "reservation"],
        "my_reservations": ["my booking", "my reservation", "my schedule"],
        "thanks": ["thanks", "thank you"]
    }

    scores = {key: 0 for key in intents}

    for intent, keywords in intents.items():
        for word in keywords:
            if word in msg:
                scores[intent] += 1

    # Return all relevant intents (not just one)
    return [k for k, v in scores.items() if v > 0]


# ==========================
# HANDLERS
# ==========================
def get_categories():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT name, description FROM categories WHERE status='Available'")
    data = cursor.fetchall()
    conn.close()

    if not data:
        return "There are no available categories right now."

    response = "Here are the available categories:\n\n"
    for name, desc in data:
        response += f"• {name} – {desc}\n"

    return response


def get_facilities():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT f.name, c.name, f.capacity, f.price_per_hour
        FROM facilities f
        JOIN categories c ON f.category_id = c.id
        WHERE f.status='Available'
    """)

    data = cursor.fetchall()
    conn.close()

    if not data:
        return "No facilities are available at the moment."

    response = "Here are the facilities you can book:\n\n"
    for name, category, cap, price in data:
        response += (
            f"🏟 {name} ({category})\n"
            f"   👥 Capacity: {cap}\n"
            f"   💰 ₱{price}/hour\n\n"
        )

    return response


def get_availability(message):
    conn = get_db()
    cursor = conn.cursor()

    date_match = re.search(r"\d{4}-\d{2}-\d{2}", message)

    if not date_match:
        return "Can you provide a date (YYYY-MM-DD) so I can check availability?"

    date = date_match.group()

    cursor.execute("""
        SELECT name FROM facilities
        WHERE id NOT IN (
            SELECT facility_id FROM reservations
            WHERE booking_date = ?
            AND status IN ('Pending','Approved')
        )
    """, (date,))

    data = cursor.fetchall()
    conn.close()

    if not data:
        return f"Looks like everything is booked on {date}."

    response = f"On {date}, these are still available:\n\n"
    for (name,) in data:
        response += f"• {name}\n"

    return response


def get_pricing():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT name, price_per_hour FROM facilities")
    data = cursor.fetchall()
    conn.close()

    response = "Here’s the pricing:\n\n"
    for name, price in data:
        response += f"• {name} — ₱{price}/hour\n"

    return response


def get_my_reservations():
    if "user_id" not in session:
        return "You need to log in first so I can check your bookings."

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT f.name, r.booking_date, r.start_time, r.end_time, r.status
        FROM reservations r
        JOIN facilities f ON r.facility_id = f.id
        WHERE r.user_id = ?
    """, (session["user_id"],))

    data = cursor.fetchall()
    conn.close()

    if not data:
        return "You don’t have any bookings yet."

    response = "Here’s what I found for your bookings:\n\n"
    for name, date, start, end, status in data:
        response += (
            f"{name} | {date} | {start}-{end} | {status}\n"
        )

    return response


# ==========================
# MAIN CHAT
# ==========================
@chatbot.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "")

    if not message:
        return jsonify({"response": "Go ahead, type something 😊"})

    intents = detect_intents(message)

    responses = []

    if "greeting" in intents:
        responses.append(random.choice([
            "Hi! How can I help you today?",
            "Hello 👋 What do you need?",
            "Hey there! 😊"
        ]))

    if "categories" in intents:
        responses.append(get_categories())

    if "facilities" in intents:
        responses.append(get_facilities())

    if "availability" in intents:
        responses.append(get_availability(message))

    if "pricing" in intents:
        responses.append(get_pricing())

    if "reservation" in intents:
        responses.append("You can book a facility by selecting a date, time, and completing payment.")

    if "my_reservations" in intents:
        responses.append(get_my_reservations())

    if "thanks" in intents:
        responses.append(random.choice([
            "You're welcome!",
            "Anytime 😊",
            "Happy to help!"
        ]))

    # SMART FALLBACK
    if not responses:
        responses.append(
            "I can help with facilities, bookings, pricing, or availability. What would you like to know?"
        )

    final_response = "\n\n".join(responses)

    return jsonify({"response": humanize(final_response)})