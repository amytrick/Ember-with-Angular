#!/usr/bin/env python3

from flask import Flask, jsonify, request 
import crud
from model import connect_to_db
from flask_cors import CORS
from datetime import datetime
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

# set Cloudinary API configurations
cloudinary.config(
                  cloud_name=os.environ.get('CLOUD_NAME'),
                  api_key=os.environ.get('API_KEY'),
                  api_secret=os.environ.get('API_SECRET')
                  )

app = Flask(__name__)
CORS(app)

@app.route('/api/upload-photo', methods = ['POST'])
def upload_photo():
    #image = request.files['photo-upload']
    photo_path = request.json['photo_path']
    # result = cloudinary.uploader.upload(image, image_metadata=True, categorization = "google_tagging", auto_tagging = 0.6)
    # result = cloudinary.uploader.upload(image, image_metadata=True, categorization = "aws_rek_tagging", auto_tagging = 0.7)
    result = cloudinary.uploader.upload(photo_path, image_metadata=True)
    # result["tags"] = ['forest','adventure']
    print(result)
    # user_id = 1
    # date_uploaded = datetime.now()
    # date_taken = datetime.strptime(result['image_metadata']['DateTimeOriginal'], "%Y:%m:%d %H:%M:%S")
    # album_id = None
    # path = result['url']
    # public_id = result['public_id']
    # photo = crud.create_photo(user_id, date_uploaded, date_taken, album_id, path, public_id)
    return jsonify({})

@app.route('/api/get-albums/<int:user_id>', methods = ['GET'])
def get_albums_by_user_id(user_id):
    albums = crud.get_albums_by_user_id(user_id)
    return jsonify([album.to_dict() for album in albums])


@app.route("/api/get-photos/album/<int:album_id>", methods = ['GET'])
def get_photos_by_album_id(album_id):
    album = crud.get_album_by_id(album_id)
    return jsonify([photo.to_dict() for photo in album.photos])

@app.route("/api/get-album/<int:album_id>", methods = ['GET'])
def get_album_by_album_id(album_id):
    album = crud.get_album_by_id(album_id)
    return jsonify(album.to_dict())

@app.route("/api/get-photo/<int:photo_id>", methods = ['GET'])
def get_photo_by_photo_id(photo_id):
    photo = crud.get_photo_by_id(photo_id)
    return jsonify(photo.to_dict())

@app.route("/api/library/<int:user_id>", methods = ['GET'])
def get_photos_by_user_id(user_id):
    photos = crud.get_photos_by_user_id(user_id)
    return jsonify([photo.to_dict() for photo in photos])

@app.route("/api/get-tags/<int:photo_id>", methods = ["GET"])
def get_tags_by_photo_id(photo_id):
    tags = crud.display_tags_by_photo_id(photo_id)
    print(tags)
    for tag in tags:
        print(tag.tag_id, tag.tagword)
        print(tag.to_dict())
    return jsonify([tag.to_dict() for tag in tags])

@app.route("/api/assign-tag", methods = ["POST"])
def assign_tag_to_photo():
    crud.add_tag_to_photo(request.json['photo_id'], request.json['tagword'])
    return jsonify({})

@app.route("/api/update-rating", methods = ["POST"])
def update_rating():
    print("Update rating")
    if not request.json:
        # todo return right codes
        return jsonify({'status': 'error'}), 201
    crud.give_rating(request.json['photo_id'],request.json['rating'])
    return jsonify({'status': 'rating updated'}), 201

@app.route("/api/filter", methods = ["POST"])
def setFilter():
    rating = request.json['rating']
    equality_symbol = request.json['equality']
    user_id = request.json['user_id']
    photos = crud.filter_photos_by_rating(rating, equality_symbol, user_id)

    return jsonify([photo.to_dict() for photo in photos])

@app.route("/api/add-album", methods = ["POST"])
def add_album():
    user_id = request.json['user_id']
    album_name = request.json['name']
    date_created = datetime.utcfromtimestamp(request.json['datetime']/1000)
    album = crud.create_album(album_name, date_created, user_id)
    
    return jsonify(album.to_dict())

@app.route("/api/add-to-album", methods = ["POST"])
def add_to_album():
    photo_id = request.json['photo_id']
    album_id = request.json['album_id']
    crud.add_to_photoalbum(photo_id, album_id)

    return jsonify({})
    

if __name__ == "__main__":
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)

