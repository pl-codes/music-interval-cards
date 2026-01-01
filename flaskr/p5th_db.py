import sqlite3

def get_p5th_connection():
    conn = sqlite3.connect("flaskr/p5th.db")
    return conn

def select_card(card_id):
    conn = get_p5th_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM p5th WHERE ROWID = ?", (card_id,))
    row = cursor.fetchone()
    conn.close()
    return row

'''
def db_length():
'''