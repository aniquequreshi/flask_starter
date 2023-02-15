from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='templates')

@site.route("/")
def home():
    # return ('home')
    return render_template('site/home.html', logged_in=True)

