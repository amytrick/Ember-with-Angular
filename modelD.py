"""Models for photo management app"""
import datetime
# from flask_sqlalchemy import SQLAlchemy

from django.db import models
# db = SQLAlchemy ()

class User(models.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Integer, primary_key=True, autoincrement=True
    fname = db.CharField(max_length=20)
    lname = db.CharField(max_length=20)
    email = db.CharField(max_length=30), unique=True
    password = db.CharField(max_length=20)

    def __str__(self):
        return self.user_id, self.email

class Photo(models.Model):
    """A photo image"""

    __tablename__ = "photos"

    photo_id = models.Integer, primary_key=True, autoincrement=True
    user_id = models.Integer, models.ForeignKey(User, on_delete=models.CASCADE)
    date_uploaded = models.DateField
    date_taken = models.DateField
    date_edited = models.DateField
    album_id = models.Integer, models.ForeignKey(Album, on_delete=models.CASCADE)
    tags = models.Integer
    # ? Not sure how to link this
    path = models.CharField(max_length=100)
    size = models.Integer
    rating = models.Integer
    # user_id, date_uploaded, date_taken, date_edited, album_id, tags, path, size, rating

    def __str__(self):
        return self.photo_id
        # ? Add more info to repr?

class Phototag(models.Model):
    """A tag on a photo - middle table between photos and tags"""

    __tablename__ = "phototags"

    phototag_id = models.Integer, primary_key=True, autoincrement=True
    photo_id = models.Integer, models.ForeignKey(Photo, on_delete=models.CASCADE)
    tag_id = models.Integer, models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.phototag_id

class Tag(models.Model):
    """A keyword to describe a photo"""

    __tablename__ = "tags"

    tag_id = models.Integer, primary_key=True, autoincrement=True
    tagword = models.CharField(max_length=30), unique=True

    def __str__(self):
        return self.tag_id, self.tagword

class Photoalbum(models.Model):
    """A photoalbum - middle table between photos and albums"""

    __tablename__ = "photoalbums"

    photoalbum_id = models.Integer, primary_key=True, autoincrement=True
    photo_id = models.Integer, models.ForeignKey(Photo, on_delete=models.CASCADE)
    album_id = models.Integer, models.ForeignKey(Album, on_delete=models.CASCADE)


    def __str__(self):
        return self.photoalbum_id

class Album(models.Model):
    """An album"""

    __tablename__ = "albums"

    album_id = models.Integer, primary_key=True, autoincrement=True
    name = models.CharField(max_length=20), unique=True
    date_created = models.DateField

    def __str__(self):
        return self.album_id, self.name


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