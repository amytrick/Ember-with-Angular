""" CRUD operations"""
import datetime
from model import db, User, Photo, Phototag, Tag, Photoalbum, Album, connect_to_db

def create_user(fname, lname, email, password):
    """Create and return a new user"""
  
    user = User(fname=fname, lname=lname, email=email, password=password)
   
    db.session.add(user)
    db.session.commit()

    return user
    

def create_photo(date_uploaded, date_taken, path):
    """Create and return photo instance"""

    photo = Photo(date_uploaded=date_uploaded, date_taken=date_taken, path=path)

    db.session.add(photo)
    db.session.commit()

    return photo


def display_all_photos():

    photos = Photo.query.all()

    return photos


def get_user_by_email(email):
    """ Return user's profile"""

    return User.query.filter(User.email == email).first()
    # user0@test.com --> {'email_1': 'user0@test.com', 'param_1': 1}


def get_id_by_email(email):
    """Return user's id"""

    user = get_user_by_email(email)
    return user.user_id


def check_password(email, password):
    """ Compare password on file for a user when they are logging in"""

    user_info = get_user_by_email(email)
    return user_info.password == password


if __name__ == '__main__':
    from server import app
    connect_to_db(app)

