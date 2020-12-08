"""Server for photo management app."""

import os
from flask import Flask, render_template, request, flash, session, redirect, json, jsonify
from model import connect_to_db
import crud
from datetime import datetime


import cloudinary
import cloudinary.uploader
import cloudinary.api


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


current_photo_list = []
current_index_clicked = None


def get_current_idx(photo_list, photo_id):
    for idx, photo in enumerate(photo_list):
        if photo.photo_id == int(photo_id):
            return idx
    return None

#################################
##         HOME/LOGIN          ##
#################################


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
    # return json.dumps({'status':'OK','user':fname,'pass':password});


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
            return redirect("/library")
            # return json.dumps({'status':'OK','email':email,'pass':password});


@app.route("/logout", methods=["POST"])
def logout():
    """Logs user out and sends them back to landing/login page"""

    session['user_id'] = None

    return create_landingpage()


#################################
##       LIBRARY ROUTES        ##
#################################


@app.route("/library")
def display_library():
    """Display all photos and list albums belonging to a user"""

    current_user_id = session.get('user_id', None)

    if current_user_id is None:
        return redirect("/")

    photos = crud.get_photos_by_user_id(current_user_id)
    albums = crud.get_albums_by_user_id(current_user_id)

    for photo in photos:
        photo.print_date = crud.print_date(photo.photo_id)

    global current_photo_list
    current_photo_list = photos
    return render_template("library.html", photos=photos, albums=albums)


@app.route("/print-date")
def print_date(photo_id):
    """Give formatted date for specific photo"""
    for photo in current_photo_list:
        date = crud.print_date(photo_id)

    return date


@app.route("/upload_photo", methods=["POST"])
def upload_new_photo():
    """User selects new photo to upload"""
    image = request.files['photo-upload']
    # result = cloudinary.uploader.upload(image, image_metadata=True, categorization = "google_tagging", auto_tagging = 0.6)
    # result = cloudinary.uploader.upload(image, image_metadata=True, categorization = "aws_rek_tagging", auto_tagging = 0.7)
    result = cloudinary.uploader.upload(image, image_metadata=True)
    #result["tags"] = ['forest','adventure']
    user_id = session['user_id']
    date_uploaded = datetime.now()
    date_taken = datetime.strptime(result['image_metadata']['DateTimeOriginal'], "%Y:%m:%d %H:%M:%S")
    album_id = None
    path = result['url']
    public_id = result['public_id']
    photo = crud.create_photo(user_id, date_uploaded, date_taken, album_id, path, public_id)
    for tagword in result["tags"]:
        crud.add_tag_to_photo(photo.photo_id, tagword)
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


@app.route("/return_to_library")
def return_to_library():
    return redirect("/library")


#################################
##     PHOTO DETAIL ROUTES     ##
#################################


@app.route("/photodetails/<photo_id>")
def display_photo(photo_id):
    """Display selected photo enlarged"""

    photo = crud.get_photo_by_id(photo_id)
    albums = crud.get_albums_by_user_id(session.get('user_id'))
    tags = crud.display_tags_by_photo_id(photo_id)
    set_of_tags = set(tags)
    date = crud.print_date(photo_id)

    global current_index_clicked
    current_index_clicked = get_current_idx(current_photo_list, photo_id)
    return render_template("photo_details.html", photo=photo, albums=albums, tags=set_of_tags, date=date)


@app.route("/delete_photo/<photo_id>", methods=["POST"])
def delete_photo(photo_id):
    photo = crud.get_photo_by_id(photo_id)

    if photo.public_id != "":
        destroy_result = cloudinary.uploader.destroy(photo.public_id)

    crud.delete_photo_by_id(photo_id)

    return redirect("/library")


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

    rating = int(request.form.get("star-radios"))

    crud.give_rating(photo_id, rating)

    return display_photo(photo_id)


@app.route("/tag/<photo_id>", methods=["POST"])
def assign_tag(photo_id):
    """Assigns tag (keyword) to specific photo"""

    tagword = (request.form.get("tag-text"))

    crud.add_tag_to_photo(photo_id, tagword)

    return display_photo(photo_id)


@app.route("/delete-tag/<photo_id>/<tag_id>")
def delete_tag(photo_id, tag_id):

    crud.remove_tag(tag_id, photo_id)

    return display_photo(photo_id)



@app.route("/next.json")
def next_photo():
    global current_index_clicked
    current_index_clicked += 1
    # next_idx = current_index_clicked + 1
    # the overflow case
    if current_index_clicked == len(current_photo_list):
        current_index_clicked = 0
    next_photo = current_photo_list[current_index_clicked]
    tags = set(crud.display_tags_by_photo_id(next_photo.photo_id))
    tag_ids = [tag.tag_id for tag in tags]
    tags = [tag.tagword for tag in tags]
    return jsonify(photo_path=next_photo.path, photo_rating=next_photo.rating, photo_id=next_photo.photo_id, tags=list(tags), tag_ids=tag_ids)
    # return redirect(f"/photodetails/{next_photo.photo_id}")


@app.route("/previous.json")
def previous_photo():
    global current_index_clicked
    current_index_clicked -= 1
    prev_photo = current_photo_list[current_index_clicked]
    if current_index_clicked == 0:
        current_index_clicked = len(current_photo_list)
    tags = set(crud.display_tags_by_photo_id(prev_photo.photo_id))
    tag_ids = [tag.tag_id for tag in tags]
    tags = [tag.tagword for tag in tags]
    return jsonify(photo_path=prev_photo.path, photo_rating=prev_photo.rating, photo_id=prev_photo.photo_id, tags=list(tags), tag_ids=tag_ids)
    # return redirect(f"/photodetails/{prev_photo.photo_id}")


#################################
##         ALBUM ROUTES        ##
#################################


@app.route("/library/<album_id>")
def display_album(album_id):
    """Display photos in a selected album"""

    album = crud.get_album_by_id(album_id)
    albums = crud.get_albums_by_user_id(session.get('user_id'))
    photoalbum = album.photos

    global current_photo_list
    current_photo_list = photoalbum
    return render_template("album_details.html", album=album, albums=albums, photoalbum=photoalbum)


@app.route("/rename-album/<album_id>", methods=["POST"])
def rename_album(album_id):
    """Rename existing album"""

    new_name = request.form.get("rename-album")

    crud.rename_album(album_id, new_name)

    return display_album(album_id)


@app.route("/delete-photo-from-album/<album_id>/<photo_id>")
def delete_photo_from_album(album_id, photo_id):
    """Delete selected photo from selected album"""

    crud.remove_photo_from_album(photo_id, album_id)

    return display_album(album_id)


#################################
##     SEARCH/FILTER ROUTES    ##
#################################


@app.route("/filterby/rating", methods=["POST"])
def filter_by_rating():
    """Filter photos by specified rating"""

    rating = request.form.get("filter-rating")
    equality_symbol = request.form.get("equality-symbol")
    user_id = session.get('user_id')
    albums = crud.get_albums_by_user_id(user_id)

    if equality_symbol == 'equals':
        photos = crud.get_photos_by_exact_rating(rating, user_id)
        statement = rating
    elif equality_symbol == 'greater':
        photos = crud.get_photos_with_greater_or_equal_rating(rating, user_id)
        statement = "≥ " + rating
    elif equality_symbol == 'less':
        photos = crud.get_photos_with_less_or_equal_rating(rating, user_id)
        statement = "≤ " + rating

    global current_photo_list
    current_photo_list = photos

    return render_template("filter.html", photos=photos, albums=albums, statement=statement)


@app.route("/search", methods=["POST"])
def searchpage():
    """Returns photos that match keyword search"""
    # filtered by user id

    tagword = (request.form.get("search")).capitalize()
    user_id = session.get('user_id')
    albums = crud.get_albums_by_user_id(user_id)
    tag = crud.get_tag_by_tagword(tagword)
    if tag:
        photos = crud.get_photos_by_tag(tag, user_id)
    else:
        photos = []

    global current_photo_list
    current_photo_list = photos
    return render_template("search-results.html", photos=photos, albums=albums, tagword=tagword)



if __name__ == "__main__":
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)

