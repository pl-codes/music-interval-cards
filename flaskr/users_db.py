import sqlite3

def insert_user(username, email, password):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        #password to be hashed in future
        cursor.execute("""
                       INSERT INTO users (username, email, password) 
                       VALUES (?, ?, ?)
                    """, (username, email, password))
        conn.commit()
        conn.close()



'''
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL UNIQUE,
               email TEXT NOT NULL UNIQUE,
               password TEXT NOT NULL
               )
               """)

conn.commit()
conn.close()
'''