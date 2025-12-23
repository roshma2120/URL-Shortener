import sqlite3

def get_connection():
    return sqlite3.connect("urls.db", check_same_thread=False)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE,
            long_url TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_url(code, long_url):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO urls (code, long_url) VALUES (?, ?)",
        (code, long_url)
    )
    conn.commit()
    conn.close()

def get_url(code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT long_url FROM urls WHERE code = ?",
        (code,)
    )
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
