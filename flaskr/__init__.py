import os
from flask import Flask, render_template, redirect, url_for, jsonify, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from flaskr.users_db import insert_user, user_exists, user_exists_email
from flaskr.card_app import random_number, process_card
import sqlite3

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    os.makedirs(app.instance_path, exist_ok=True)

    # One-time initializing script to create the users.db database
    @app.cli.command("create_db")    
    def create_db():
        db =  os.path.join(app.instance_path, "users.db")
        conn = sqlite3.connect(db)
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

    class RegisterForm(FlaskForm):
        '''
        Form for users to register.
        '''
        username = StringField('Username', validators=[
            DataRequired(), Regexp(r'^(?=.*[a-zA-Z])[a-zA-Z0-9_]{2,30}$', message='2-30 characters, letters, numbers, underscores only—with at least one letter.')
            ])
        email = StringField('Email', validators=[DataRequired(), Email(granular_message=False)])
        password = PasswordField('Password', validators=[
            DataRequired(), Regexp(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,64}$', message='8-64 characters and must include at least one uppercase letter, one lowercase letter, and one number.')
            ])
        confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
        submit = SubmitField('Register')

    class LoginForm(FlaskForm):
        '''
        Form for users to login.
        '''
        email = StringField('Email', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        submit = SubmitField('Submit')

    class IntervalForm(FlaskForm):
        '''
        Form for users to select the musical interval to practice.
        '''
        choice = RadioField("Choose Interval",
                            choices=[('p5th', 'Perfect 5th'), ('p4th', 'Perfect 4th')],
                            validators=[DataRequired()]
                            )
        submit = SubmitField('Begin')


    @app.route('/', methods=["GET", "POST"])    
    def index():
        '''
        The welcome page, where the user can select the musical interval to practice.
        Once selected, it is validated and stored into a session. Then user is directed to the "play" page. 
        '''
        form = IntervalForm()
        if form.validate_on_submit():
            selection = form.choice.data
            session["interval_selection"] = selection
            return redirect(url_for('play'))
        return render_template('index.html', form=form)
            

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        '''
        The registration page, where a new user can register.
        After the form is filled out and submitted, it is validated and routed to the "success" page.
        '''
        form = RegisterForm()
        if form.validate_on_submit():            
            username = form.username.data
            email = form.email.data
            password = form.password.data
            confirm_password = form.confirm_password.data            

            print(f"Username: {username}")
            print(f"Email: {email}")
            print(f"Password: {password}")
            print(f"Confirmed Password: {confirm_password}")

            does_exist = user_exists_email(email)

            if does_exist == True:
                return render_template('register-form2.html', form=form, error="An account with this email already exists")
            else:
                insert_user(username, email, password) 
                return redirect(url_for("success"))
            
        return render_template('register-form2.html', form=form, error=None)
    
    
    @app.route('/terms')
    def terms():
        return render_template("terms.html")


    @app.route('/success')
    def success():
        '''
        Displays successful message.
        '''
        return render_template('register-go.html')
    
        
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        '''
        The login page, where a registered user can sign in.
        '''
        form = LoginForm()
        if form.validate_on_submit():            
            email = form.email.data
            password = form.password.data
            print(f"Email: {email}")
            print(f"Password: {password}")
            
            does_exist = user_exists(email, password)           

            if does_exist == True:
                return redirect(url_for("index"))
            else: 
                return render_template('login.html', form=form, error="Invalid email or password")
            
        return render_template('login.html', form=form, error=None)
    
    
    @app.route('/play', methods=["GET", "POST"])
    def play():
        '''
        Displays card_play page.
        '''        
        return render_template('card_play.html')
    

    @app.route('/start', methods=["POST"])
    def start():
        '''
        Not a displayed page. This route is called when the user presses start.
        First the total amount of cards in the deck (database) are determined and the cards are shuffled (randomized).
        Then the first card is selected for the user.
        Returns card information.
        '''        
        interval_selection = session["interval_selection"]

        session["row_numbers"], total_cards = random_number(interval_selection) #Process to randomize the cars and determine total amount of cards in the deck.     
        row_numbers = session["row_numbers"]        

        remaining_rows, card_values, cards_left = process_card(interval_selection, row_numbers) #Process to select a card and card info.
               
        session["row_numbers"] = remaining_rows        

        return jsonify({            
            "card_values": card_values,
            "total_cards": total_cards,
            "cards_left": cards_left,
            "interval_selection": interval_selection
            })
    
    
    @app.route('/next', methods=["POST"])
    def next():
        '''
        Not a displayed page. This route is called when the user presses next.
        The next card is selected for the user.
        Returns card information.
        '''
        row_numbers = session["row_numbers"]
        interval_selection = session["interval_selection"]

        remaining_rows, card_values, cards_left = process_card(interval_selection, row_numbers) #Process to select a card
        
        session["row_numbers"] = remaining_rows

        return jsonify({            
            "card_values": card_values,
            "cards_left": cards_left
            })
    
    return app