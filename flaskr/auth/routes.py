from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route("/sign_up")
def sign_up():
    return render_template('auth/sign_up.html')

@auth.route("/logout")
def logout():
    return render_template('auth/logout.html')
