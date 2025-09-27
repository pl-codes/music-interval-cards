from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    class RegisterForm(FlaskForm):
        username = StringField('Username', validators=[
            DataRequired(), Length(min=2, max=30), Regexp('^(?=.*[a-zA-Z])[a-zA-Z0-9_]+$', message='Letters, numbers, underscores only—with at least one letter.')
            ])
        email = StringField('Email', validators=[DataRequired(), Email(granular_message=True)])
        password = PasswordField('Password', validators=[
            DataRequired(), Regexp('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).+$', message='Include at least one uppercase letter, one lowercase letter, and one number.'), Length(min=8, max=64), EqualTo('confirm_password', message='Passwords must match.')
            ])
        confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
        submit = SubmitField('Register')


    @app.route('/', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            confirm_password = form.confirm_password.data
            return redirect(url_for("success"))
        return render_template('register-form.html', form=form)
    
    @app.route('/success')
    def success():
        return "Registration successful!"
    

    '''
    def user_info():
        if request.method == 'POST':
            name = request.form.get('name')            
            email = request.form.get('email')
            pswd = request.form.get('pswd')
            pswd_repeat = request.form.get('pswd-repeat')

            print(name, email, pswd, pswd_repeat)            
            return f'Info received'
        else:
            return render_template('register-form.html')
    '''

    return app