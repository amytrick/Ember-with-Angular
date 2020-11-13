""" CRUD operations"""
import datetime
from model import db, User, Photo, Phototag, Tag, Photoalbum, Album, connect_to_db

## CREATING NEW OBJECTS ##

def create_user(fname, lname, email, password):
    """Create and return a new user"""
  
    user = User(fname=fname, lname=lname, email=email, password=password)
   
    db.session.add(user)
    db.session.commit()

    return user
    

def create_photo(user_id, date_uploaded, date_taken, album_id, path):
    """Create and return photo instance"""

    photo = Photo(user_id=user_id, date_uploaded=date_uploaded, date_taken=date_taken, album_id=album_id, path=path)

    db.session.add(photo)
    db.session.commit()

    return photo


def create_album(name, date_created):
    """Create new album to be added to db"""

    album = Album(name=name, date_created=date_created)

    db.session.add(album)
    db.session.commit()

    return album


## PHOTO RELATED QUERIES ##

def display_all_photos():

    photos = Photo.query.all()

    return photos


def get_photos_by_album_id(album_id):
    """Return all photos that have a specific, selected album id"""

    photos = Photo.query.filter(Photo.album_id == album_id).all()

    return photos


def get_photo_by_id(photo_id):
    """Return photo by querying with photo id"""

    photo = Photo.query.get(photo_id)

    return photo


## ALBUM RELATED QUERIES ##

def display_all_albums():
    """Display all albums in Album db"""

    albums = Album.query.all()

    return albums


def get_album_by_id(album_id):
    """Return album object by querying with album id"""

    album = Album.query.get(album_id)
    return album


# def add_photo_to_album(photo_id, album_id):
#     """Add selected photo to an existing album"""

#     photo = get_photo_by_id(photo_id)
#     photo.album_id = album_id
#     db.session.commit()


def add_to_photoalbum(photo_id, album_id):
    """Add photo to photoalbum table"""

    photoalbum = Photoalbum(photo_id=photo_id, album_id=album_id)

    db.session.add(photoalbum)
    db.session.commit()

    return photoalbum


def display_photoalbum(album_id):
    """Return all photos (from photoalbum db) that are associated with a specific album"""
    photos = []
    photoalbum = Photoalbum.query.filter(Photoalbum.album_id == album_id).all()
    for item in photoalbum:
        photo = get_photo_by_id(item.photo_id)
        photos.append(photo)

    return photos


def get_album_by_name(name):
    """Return album object by querying with album name"""

    album = Album.query.filter(Album.name == name).first()

    return album

## TODO give ability for user to change album name
    # def rename_album(currentAlbumName)


## USER RELATED QUERIES ##

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


## RATINGS ##

def give_rating(photo_id, rating):
    """Return photo with a newly added/updated rating"""

    photo = get_photo_by_id(photo_id)
    photo.rating = rating
    db.session.commit()

### USING UPDATE -- CAN BE MORE HELPFUL WHEN CHANGING MULTIPLE THINGS AT ONCE ###
        # admin = User.query.filter_by(username='admin').update(dict(email='my_new_email@example.com')))
        # db.session.commit()
     
### SIMPLY CHANGING THE FIELD ENTITY -- USEFUL FOR CHANGING ONE THING AT A TIME ###
        # admin = User.query.filter_by(username='admin').first()
        # admin.email = 'my_new_email@example.com'
        # db.session.commit()

        # user = User.query.get(5)
        # user.name = 'New Name'
        # db.session.commit()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)

