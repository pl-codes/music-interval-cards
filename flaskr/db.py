import sqlite3

def get_connection(data_base):
    conn = sqlite3.connect(f"flaskr/{data_base}.db")
    return conn

def select_card(card_id, interval_selection):
    conn = get_connection(interval_selection)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {interval_selection} WHERE ROWID = ?", (card_id,))
    row = cursor.fetchone()
    conn.close()
    return row


def row_count(interval_selection):
    conn = get_connection(interval_selection)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {interval_selection}")
    total_rows = cursor.fetchone()[0]
    return total_rows
