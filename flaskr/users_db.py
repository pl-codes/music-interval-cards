import sqlite3
import os
from flask import current_app

def get_connection():
        db =  os.path.join(current_app.instance_path, "users.db")
        conn = sqlite3.connect(db)
        return conn


def insert_user(username, email, password):
        '''
        Purpose: Inserts new user into the users.db database
        
        :param username: User's username
        :param email: User's email
        :param password: User's password (to be hashed in the future)
        '''
        conn = get_connection()
        cursor = conn.cursor()
        #password to be hashed in future
        cursor.execute("""
                       INSERT INTO users (username, email, password) 
                       VALUES (?, ?, ?)
                    """, (username, email, password))
        conn.commit()
        conn.close()

def user_exists_email(email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT 1 FROM users
                       WHERE email = (?)
                       """, (email,))
        does_exist = cursor.fetchone()
        conn.close()
        return does_exist is not None

def user_exists(email, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT 1 FROM users
                       WHERE email = (?)  AND password = (?)
                       """, (email, password))
        does_exist = cursor.fetchone()
        conn.close()
        return does_exist is not None

def user_exists_info(email, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT email, password FROM users
                       WHERE email = (?)  AND password = (?)
                       """, (email, password))
        row = cursor.fetchone()
        if row is not None:
                check_email, check_password = row
        conn.close()
        return check_email, check_password