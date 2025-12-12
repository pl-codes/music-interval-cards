import sqlite3

def get_p5th_connection():
    conn = sqlite3.connect("p5th.db")
    return conn

def select_card():
    conn = get_p5th_connection()
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM ")