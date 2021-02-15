from flask import Flask, jsonify, request 
import crud
from model import connect_to_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/get_albums/<int:user_id>', methods = ['GET'])
def get_albums_by_user_id(user_id):
    albums = crud.get_albums_by_user_id(user_id)
    return jsonify([album.to_dict() for album in albums])


if __name__ == "__main__":
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)

