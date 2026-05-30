import sqlite3
from config import DB_NAME
from datetime import datetime

ALLOWED_ACTIONS = {'create', 'update', 'delete', 'insert', 'add', 'edit', 'remove'}

def format_logs(logs):
    formatted = []
    for log in logs:
        dt = datetime.strptime(log["created_at"], "%Y-%m-%d %H:%M:%S")
        log["date"] = dt.strftime("%B %d, %Y")
        log["time"] = dt.strftime("%I:%M %p")
        formatted.append(log)
    return formatted

def log_action(action, table_name, record_id=None, description=None):
    """Only logs CRUD operations. Silently ignores anything else."""
    if action.lower() not in ALLOWED_ACTIONS:
        return

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO history_log (action, table_name, record_id, description)
            VALUES (?, ?, ?, ?)
        """, (action, table_name, record_id, description))
        conn.commit()
        conn.close()
    except Exception as e:
        print("History Log Error:", e)