from flask import Flask, render_template, redirect, url_for, jsonify, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from flaskr.users_db import insert_user
from flaskr.card_app import random_number, process_card, get_row
import sqlite3

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'    

    class RegisterForm(FlaskForm):
        username = StringField('Username', validators=[
            DataRequired(), Regexp('^(?=.*[a-zA-Z])[a-zA-Z0-9_]{2,30}$', message='2-30 characters, letters, numbers, underscores only—with at least one letter.')
            ])
        email = StringField('Email', validators=[DataRequired(), Email(granular_message=False)])
        password = PasswordField('Password', validators=[
            DataRequired(), Regexp('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,64}$', message='8-64 characters and must include at least one uppercase letter, one lowercase letter, and one number.')
            ])
        confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
        submit = SubmitField('Register')    

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():            
            username = form.username.data
            email = form.email.data
            password = form.password.data
            confirm_password = form.confirm_password.data

            insert_user(username, email, password)

            print(f"Username: {username}")
            print(f"Email: {email}")
            print(f"Password: {password}")
            print(f"Confirmed Password: {confirm_password}")
            
            return redirect(url_for("success"))
        return render_template('register-form.html', form=form)
    
    @app.route('/success')
    def success():
        return "Registration successful!"
    
    @app.route('/play')
    def play():
        return render_template('card_play.html')

    @app.route('/start', methods=["POST"])
    def start():        
        session["row_numbers"] = random_number()
        row_numbers = session["row_numbers"]
        total_cards = len(row_numbers)

        remaining_rows, card_values, cards_left = process_card(row_numbers)
               
        session["row_numbers"] = remaining_rows        

        return jsonify({
            "status": "started",
            "card_values": card_values,
            "total_cards": total_cards,
            "cards_left": cards_left
            })
    
    @app.route('/next', methods=["POST"])
    def next():
        row_numbers = session["row_numbers"]

        remaining_rows, card_values, cards_left = process_card(row_numbers)
        
        session["row_numbers"] = remaining_rows

        return jsonify({
            "status": "started",
            "card_values": card_values,
            "cards_left": cards_left
            })
    
    return app