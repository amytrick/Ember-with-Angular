"""Models for photo management app"""
import datetime
from flask_sqlalchemy import SQLAlchemy

# The name of my db : createdb photos

db = SQLAlchemy ()

class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(20))

    photo = db.relationship('Photo')

    def __repr__(self):
        return f"<User user_id = {self.user_id} email = {self.email}>"

class Photo(db.Model):
    """A photo image"""

    __tablename__ = "photos"

    photo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    date_uploaded = db.Column(db.DateTime)
    date_taken = db.Column(db.DateTime)
    date_edited = db.Column(db.DateTime)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.album_id"))
    tags = db.Column(db.Integer)
    # ? Not sure how to link this
    path = db.Column(db.String)
    size = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    # user_id, date_uploaded, date_taken, date_edited, album_id, tags, path, size, rating

    user = db.relationship('User')
    phototag = db.relationship('Phototag')
    photoalbum = db.relationship('Photoalbum')

    def __repr__(self):
        return f"<Photo photo_id = {self.photo_id}>"
        # ? Add more info to repr?

class Phototag(db.Model):
    """A tag on a photo - middle table between photos and tags"""

    __tablename__ = "phototags"

    phototag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    photo_id = db.Column(db.Integer, db.ForeignKey("photos.photo_id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.tag_id"))

    photo = db.relationship('Photo')
    tag = db.relationship('Tag')

    def repr(self):
        return f"<Phototag phototag_id = {self.phototag_id}>"

class Tag(db.Model):
    """A keyword to describe a photo"""

    __tablename__ = "tags"

    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tagword = db.Column(db.String(20), unique=True)

    def repr(self):
        return f"<Tag tag_id = {self.tag_id} tagword = {self.tagword}>"

    phototag = db.relationship('Phototag')

class Photoalbum(db.Model):
    """A photoalbum - middle table between photos and albums"""

    __tablename__ = "photoalbums"

    photoalbum_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    photo_id = db.Column(db.Integer, db.ForeignKey("photos.photo_id"))
    album_id = db.Column(db.Integer, db.ForeignKey("albums.album_id"))

    photo = db.relationship('Photo')
    album = db.relationship('Album')

    def repr(self):
        return f"<Photoalbum photoalbum_id = {self.photoalbum_id}>"

class Album(db.Model):
    """An album"""

    __tablename__ = "albums"

    album_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    date_created = db.Column(db.DateTime)

    photoalbum = db.relationship('Photoalbum')

    def repr(self):
        return f"<Album album_id = {self.album_id} name = {self.name}>"


def connect_to_db(flask_app, db_uri="postgresql:///photos", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

#   test_user = User(fname='Jane', lname='Tester', email='jtester@test.com', password='123')
#   photo1 = Photo(user_id=1, date_uploaded=datetime.datetime.now())

