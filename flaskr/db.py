import sqlite3

def get_connection(data_base):
    '''
    Purpose: To connect to the database
    
    :param data_base: The database file name
    '''
    conn = sqlite3.connect(f"flaskr/{data_base}.db")
    return conn

def select_card(card_id, interval_selection):
    '''
    Purpose: To select a specific card from the database.
    
    :param card_id: The row number used locate the card info in the database.
    :param interval_selection: This is used as the table name of the database.
    '''
    conn = get_connection(interval_selection)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {interval_selection} WHERE ROWID = ?", (card_id,))
    row = cursor.fetchone()
    conn.close()
    return row


def row_count(interval_selection):
    '''
    Purpose: 
        To get the total number of cards of the database.
        (Used to determine the total initial number of cards at the start of the game.)
    
    :param interval_selection: This is used as the table name of the database.
    '''
    conn = get_connection(interval_selection)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {interval_selection}")
    total_rows = cursor.fetchone()[0]
    return total_rows
