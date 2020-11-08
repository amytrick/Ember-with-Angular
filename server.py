"""Server for photo management app."""

import os
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

# set Cloudinary API configurations
cloudinary.config(
                  cloud_name = os.environ.get('CLOUD_NAME'), 
                  api_key = os.environ.get('API_KEY'), 
                  api_secret = os.environ.get('API_SECRET')
                  )
# cloudinary.config( 
#                   cloud_name = "dv77rliti", 
#                   api_key = "213853632381728", 
#                   api_secret = "QV24_tQRUyGwSl5UoDt9jd01SYk")


@app.route("/")
def create_landingpage():
    """Return landing page with cover photo and login/sign up options"""

    return render_template("landingpage.html")

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
        photos = crud.display_all_photos() 
        return render_template("library.html", photos=photos)
    else:
        flash('Incorrect password! Try again')
        return redirect ("/")

@app.route('/session')
def set_session():
    """Set value for session['user_id']"""

    email = request.args.get("login_email")
    user = crud.get_user_by_email(email)
    user_id = user.user_id

    session['user_id'] = user_id
    session['email'] = email

    return redirect("/")


@app.route('/session/get')
def get_session():
    """Get values out of session"""

    user_id = session['user_id']
    email = session['email']


@app.route("/library", methods=["POST"])
def add_photo_to_library():

    photos = crud.display_all_photos()

    return render_template("library.html", photos=photos)

@app.route("/library")
def display_library():

    photos = crud.display_all_photos()

    return render_template("library.html", photos=photos)


@app.route("/create_photo")
def create_new_photo():

    upload_file = upload(file,
                             folder = f"user/{session['user_email']}",
                             unique_filename = 1,
                             # background_removal = "cloudinary_ai",
                             )

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)