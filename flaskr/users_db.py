import sqlite3
import os
from flask import current_app

def insert_user(username, email, password):
        '''
        Purpose: Inserts new user into the users.db database
        
        :param username: User's username
        :param email: User's email
        :param password: User's password (to be hashed in the future)
        '''

        db =  os.path.join(current_app.instance_path, "users.db")
        conn = sqlite3.connect(db)
        #conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        #password to be hashed in future
        cursor.execute("""
                       INSERT INTO users (username, email, password) 
                       VALUES (?, ?, ?)
                    """, (username, email, password))
        conn.commit()
        conn.close()