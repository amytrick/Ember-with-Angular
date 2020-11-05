"""Server for photo management app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

import cloudinary
import cloudinary.uploader
import cloudinary.api



from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "HKBuLa3wTL"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def create_coverpage():
    """Return landing page with cover photo and login/sign up options"""

    return render_template("coverpage.html")

@app.route("/user", methods=["POST"])
def add_user():
    """Add new user, redirect them to landing page to login"""
    
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")

    check_email = crud.get_user_by_email(email)

    if check_email == None:
        crud.create_user(fname, lname,email, password)
        flash("New account created successfully! Please log in")
    else:
        flash("Email is already associated with an account. Try again")


    return redirect ("/")

@app.route("/login")
def confirm_credentials():
    """Checks newly entered login credentials with those in db"""

    email = request.args.get("login_email")
    password = request.args.get("login_password")

    match_passwords = crud.check_password(email, password)
    if match_passwords == True:
        return render_template("library.html")
    else:
        flash('Incorrect password! Try again')
        return redirect ("/")

# @app.route('/session')
# def set_session():
#     """Set value for session['user_id']"""

#     user_id = get_user_by_email(email)
#     session['user_id'] = user_id


# @app.route('/session/get'):
# def get_session():
#     """Get values out of session"""

#     user_id = session['user_id']


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)