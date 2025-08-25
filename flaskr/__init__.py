from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)

    @app.route('/register', methods=['GET', 'POST'])
    def user_info():
        if request.method == 'POST':
            name = request.form.get('name')
            #last_name = request.form.get('last-name')
            email = request.form.get('email')
            pswd = request.form.get('pswd')
            pswd_repeat = request.form.get('pswd-repeat')

            print(name, email, pswd, pswd_repeat)
            #return f'{first_name}, {last_name}, {email} {pswd}, {pswd_repeat}'
            return f'Info received'
        else:
            return render_template('register-form.html')
    return app