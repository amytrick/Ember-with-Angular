from flask import Flask, jsonify, request 
import crud
from model import connect_to_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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


if __name__ == "__main__":
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)

