import sqlite3

def insert_user(username, email, password):
        '''
        Purpose: Inserts new user into the users.db database
        
        :param username: User's username
        :param email: User's email
        :param password: User's password (to be hashed in the future)
        '''
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        #password to be hashed in future
        cursor.execute("""
                       INSERT INTO users (username, email, password) 
                       VALUES (?, ?, ?)
                    """, (username, email, password))
        conn.commit()
        conn.close()