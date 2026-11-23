import sqlite3
from datetime import datetime

DB_PATH = "search_history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_image TEXT,
            result_path TEXT,
            rank INTEGER,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_search(query_image, results):
    conn = sqlite3.connect(DB_PATH)
    timestamp = datetime.now().isoformat()
    for rank, result_path in enumerate(results, start=1):
        conn.execute(
            "INSERT INTO searches (query_image, result_path, rank, timestamp) VALUES (?, ?, ?, ?)",
            (query_image, str(result_path), rank, timestamp)
        )
    conn.commit()
    conn.close()

def get_recent_searches(limit=5):
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT DISTINCT query_image, timestamp FROM searches ORDER BY timestamp DESC LIMIT ?",
        (limit,)
    ).fetchall()
    conn.close()
    return rows

init_db()
