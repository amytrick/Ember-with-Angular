"""Server for photo management app."""

import os
from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db
import crud
from datetime import datetime

import cloudinary
import cloudinary.uploader
import cloudinary.api
# import PIL
# import PIL.ExifTags
# import PIL.Image
# import copy
# from io import BytesIO

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "HKBuLa3wTL"
# app.secret_key = os.environ.get('FLASK_SECRET_KEY')
app.jinja_env.undefined = StrictUndefined

os.system('pwd')
os.system('source secrets.sh')

# set Cloudinary API configurations
cloudinary.config(
                  cloud_name=os.environ.get('CLOUD_NAME'),
                  api_key=os.environ.get('API_KEY'),
                  api_secret=os.environ.get('API_SECRET')
                  )


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

    user = crud.get_user_by_email(email)

    if not user:
        crud.create_user(fname, lname, email, password)
        flash("New account created successfully! Please log in")
    else:
        flash("Email is already associated with an account. Try again")
    return redirect("/")


@app.route("/login")
def confirm_credentials():
    """Checks newly entered login credentials with those in db"""

    email = request.args.get("login_email")
    password = request.args.get("login_password")

    match_passwords = crud.check_password(email, password)
    user = crud.get_user_by_email(email)

    if not user:
        flash('This user does not have an account - please create one')
        return redirect('/')
    else:
        if not match_passwords:
            flash('Incorrect password! Try again')
            return redirect("/")
        else:
            session['user_id'] = user.user_id
            session['email'] = user.email
            session['fname'] = user.fname
            session['lname'] = user.lname
            flash('Login successful!')
            # current_user_id = session.get('current_user')
            return redirect("/library")


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


@app.route("/library")
def display_library():
    """Display all photos and list albums belonging to a user"""

    current_user_id = session.get('user_id', None)

    if current_user_id == None:
        return redirect("/")

    photos = crud.get_photos_by_user_id(current_user_id)
    albums = crud.get_albums_by_user_id(current_user_id)

    return render_template("library.html", photos=photos, albums=albums)


@app.route("/upload_photo", methods=["POST"])
def upload_new_photo():
    """User selects new photo to upload"""
    image = request.files['test_image']
    result = cloudinary.uploader.upload(image, image_metadata=True)

    user_id = session['user_id']
    date_uploaded = datetime.now()
    date_taken = datetime.strptime(result['image_metadata']['DateTimeOriginal'], "%Y:%m:%d %H:%M:%S")
    album_id = None
    path = result['url']
    public_id = result['public_id']
    crud.create_photo(user_id, date_uploaded, date_taken, album_id, path, public_id)

    return redirect("/library")


@app.route("/photodetails/<photo_id>")
def display_photo(photo_id):
    """Display selected photo enlarged"""

    photo = crud.get_photo_by_id(photo_id)
    albums = crud.get_albums_by_user_id(session.get('user_id'))
    tags = crud.display_tags_by_photo_id(photo_id)
    set_of_tags = set(tags)

    return render_template("photo_details.html", photo=photo, albums=albums, tags=set_of_tags)


@app.route("/delete_photo/<photo_id>", methods=["POST"])
def delete_photo(photo_id):
    photo = crud.get_photo_by_id(photo_id)

    if photo.public_id != "":
        destroy_result = cloudinary.uploader.destroy(photo.public_id)

    crud.delete_photo_by_id(photo_id)

    return redirect("/library")


@app.route("/add_album")
def create_new_album():
    """Add new album, named by user"""

    name = request.args.get("new_album_name")
    date_created = datetime.now()
    user_id = session.get('user_id')

    album = crud.create_album(name, date_created, user_id)

    return redirect("/library")
    # return jsonify({'album_id' : {{album.album_id}}, 'name': {{album.name}}})


@app.route("/library/<album_id>")
def display_album(album_id):
    """Display photos in a selected album"""

    album = crud.get_album_by_id(album_id)
    photoalbum = album.photos

    return render_template("album_details.html", album=album, photoalbum=photoalbum)


@app.route("/add-to-album/<photo_id>", methods=["POST"])
def add_to_album(photo_id):
    """Add a photo to an existing album"""

    album_name = request.form.get("add-to-album")
    album = crud.get_album_by_name(album_name)
    album_id = album.album_id
    crud.add_to_photoalbum(photo_id, album_id)

    return display_photo(photo_id)


@app.route("/rating/<photo_id>", methods=["POST"])
def assign_rating(photo_id):
    """Assigns rating to selected photo"""

    rating = int(request.form.get("rating"))

    crud.give_rating(photo_id, rating)

    return display_photo(photo_id)


@app.route("/return_to_library")
def return_to_library():
    return redirect("/library")


@app.route("/tag/<photo_id>", methods=["POST"])
def assign_tag(photo_id):
    """Assigns tag (keyword) to specific photo"""

    tagword = (request.form.get("tag-text")).capitalize()
    if crud.tag_exists(tagword):
        tag = crud.get_tag_by_tagword(tagword)
    else:
        tag = crud.create_tag(tagword)
    crud.add_to_phototags(photo_id, tag.tag_id)

    return display_photo(photo_id)


@app.route("/search", methods=["POST"])
def search():
    """Returns photos that match keyword search"""

    tagword = (request.form.get("search")).capitalize()
    user_id = session.get('user_id')
    albums = crud.get_albums_by_user_id(user_id)
    tag = crud.get_tag_by_tagword(tagword)
    if tag:
        photos = crud.get_photos_by_tag(tag, user_id)
    else:
        photos = []
    return render_template("search-results.html", photos=photos, albums=albums)



if __name__ == "__main__":
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)

