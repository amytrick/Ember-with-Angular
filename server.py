"""Server for photo management app."""

import os
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from datetime import datetime

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
        # photos = crud.display_all_photos() 
        return redirect("/library")
        # render_template("library.html", photos=photos)
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
    #? What is this?

    photos = crud.display_all_photos()

    return render_template("library.html", photos=photos)


@app.route("/library")
def display_library():
    """Display all photos and list albums belonging to a user"""

    photos = crud.display_all_photos()
    albums = crud.display_all_albums()

    return render_template("library.html", photos=photos, albums=albums)


@app.route("/create_photo")
def create_new_photo():
    """User selects new photo to upload"""

    upload_file = upload(file,
                             folder = f"user/{session['user_email']}",
                             unique_filename = 1,
                             # background_removal = "cloudinary_ai",
                             )


@app.route("/add_album")
def create_new_album():
    """Add new album, named by user"""
    
    name = request.args.get("new_album_name")
    date_created = datetime.now()

    album = crud.create_album(name, date_created)

    return redirect("/library")


@app.route("/library/<album_id>")
def display_album(album_id):
    """Display photos in a selected album"""

    album = crud.get_album_by_id(album_id)
    photos = crud.get_photos_by_album_id(album_id)
    print(photos)

    return render_template("album_details.html", album=album, photos=photos)


@app.route("/<photo_id>")
def display_photo(photo_id):
    """Display selected photo"""

    photo = crud.get_photo_by_id(photo_id)

    return render_template("photo_details.html", photo=photo)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)