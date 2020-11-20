""" CRUD operations"""
from model import db, User, Photo, Phototag, Tag, Photoalbum, Album, connect_to_db
from sqlalchemy import desc
from datetime import datetime
import time

#################################
##    CREATING NEW OBJECTS     ##
#################################


def create_user(fname, lname, email, password):
    """Create and return a new user"""

    user = User(fname=fname, lname=lname, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_photo(user_id, date_uploaded, date_taken, album_id, path, public_id=''):
    """Create and return photo instance"""

    photo = Photo(user_id=user_id, date_uploaded=date_uploaded, date_taken=date_taken, album_id=album_id, path=path, public_id=public_id)

    db.session.add(photo)
    db.session.commit()

    return photo


def create_album(name, date_created, user_id):
    """Create new album to be added to db"""

    album = Album(name=name, date_created=date_created, user_id=user_id)

    db.session.add(album)
    db.session.commit()

    return album


def create_tag(tagword):
    """Create new keyword"""

    tag = Tag(tagword=tagword)

    db.session.add(tag)
    db.session.commit()

    return tag

#################################
##        PHOTO QUERIES        ##
#################################


# def display_all_photos():

#     photos = Photo.query.all()

#     return photos


# def get_photos_by_album_id(album_id):
#     """Return all photos that have a specific, selected album id"""

#     photos = Photo.query.filter(Photo.album_id == album_id).all()

#     return photos


def get_photo_by_id(photo_id):
    """Return photo by querying with photo id"""

    photo = Photo.query.get(photo_id)

    return photo


def get_photos_by_user_id(user_id):
    """Return only photos with specified user_id"""

    photos = Photo.query.filter(Photo.user_id == user_id).order_by(desc(Photo.date_taken)).all()

    return photos


def delete_photo_by_id(photo_id):
    """Query for photo by id and delete it from database"""

    photo = Photo.query.get(photo_id)
    db.session.delete(photo)
    db.session.commit()


#################################
##        ALBUM QUERIES        ##
#################################

# # TODO check if I use this
# def display_all_albums():
#     """Display all albums in Album db"""

#     albums = Album.query.all()

#     return albums


def get_album_by_id(album_id):
    """Return album object by querying with album id"""

    album = Album.query.get(album_id)
    return album

# # TODO check if I actually use this function
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

# # TODO I don't think I need this function anymore - double check before deleting
# def display_photoalbum(album_id):
#     """Return all photos (from photoalbum db) that are associated with a specific album"""
#     photos = []
#     photoalbum = Photoalbum.query.filter(Photoalbum.album_id == album_id).all()
#     for item in photoalbum:
#         photo = get_photo_by_id(item.photo_id)
#         photos.append(photo)

#     return photos


def get_album_by_name(name):
    """Return album object by querying with album name"""

    album = Album.query.filter(Album.name == name).first()

    return album


def get_albums_by_user_id(user_id):
    """Display albums owned by a user, when querying by user id"""

    albums = Album.query.filter(Album.user_id == user_id).all()
    return albums


def rename_album(album_id, new_name):
    """Allows user to rename an existing album"""

    album = Album.query.get(album_id)
    album.name = new_name
    db.session.commit()

    return album


def remove_photo_from_album(photo_id, album_id):
    """Remove a photo from an album by deleting record in photoalbum db"""

    photoalbum_record = Photoalbum.query.filter(Photoalbum.photo_id == photo_id,
                                                Photoalbum.album_id == album_id).first()

    db.session.delete(photoalbum_record)
    db.session.commit()


#################################
##         USER QUERIES        ##
#################################


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


def get_user_by_user_id(user_id):
    """Return user when querying by user id"""

    user = User.query.get(user_id)

    return user


#################################
##           RATINGS           ##
#################################

def give_rating(photo_id, rating):
    """Update photo with a newly added/updated rating"""

    photo = get_photo_by_id(photo_id)
    photo.rating = rating
    db.session.commit()


def get_photos_by_exact_rating(rating):
    """Return photos that have a specified rating"""

    photos = Photo.query.filter(Photo.rating == rating).all()

    return photos


def get_photos_with_greater_or_equal_rating(rating):
    """Return photos that have a rating greater to or equal to specified rating"""

    photos = Photo.query.filter(Photo.rating >= rating).all()

    return photos


def get_photos_with_less_or_equal_rating(rating):
    """Return photos that have a rating less to or equal to specified rating"""

    photos = Photo.query.filter(Photo.rating <= rating).all()

    return photos


#################################
##            TAGS             ##
#################################


def add_to_phototags(photo_id, tag_id):
    """Add photo with tag to phototag table"""

    phototag = Phototag(photo_id=photo_id, tag_id=tag_id)
    # photo = get_photo_by_id(photo_id)
    # photo.tags = True
    db.session.commit()

    db.session.add(phototag)
    db.session.commit()

    return phototag


def get_tag_by_id(tag_id):
    """Return a tag when querying for its id"""
    tag = Tag.query.get(tag_id)

    return tag


def get_tag_by_tagword(tagword):
    """Return tag when querying with tagword"""
    tag = Tag.query.filter(Tag.tagword == tagword).first()

    return tag


def display_tags_by_photo_id(photo_id):
    """Display all tags assigned to a specific photo"""

    tags = []
    phototags = Phototag.query.filter(Phototag.photo_id == photo_id).all()
    for item in phototags:
        tag = get_tag_by_id(item.tag_id)
        tags.append(tag)
    return tags


def tag_exists(tagword):
    """Return boolean if tag already exists in tag db"""

    return True if Tag.query.filter(Tag.tagword == tagword).first() else False


def get_photos_by_tag(tag, user_id):
    """Return photos that have been tagged with tagword, for particular user"""

    tagged_photos = tag.photos
    photos = []
    for photo in tagged_photos:
        if photo.user_id == user_id:
            photos.append(photo)

    return photos


def get_phototag_record(photo_id, tag_id):
    """Find phototag record when filtering with photo id and tag id"""

    phototag = Phototag.query.filter(Phototag.photo_id == photo_id, Phototag.tag_id == tag_id).first()

    return phototag


def remove_tag(tag_id, photo_id):
    """Remove specific tag from specified photo by deleting photoalbum entry"""

    # tag = get_tag_by_id(tag_id)
    phototag = get_phototag_record(photo_id, tag_id)

    db.session.delete(phototag)
    db.session.commit()


def print_date(photo_id):
    """Use a photo's date_taken to print out a nicely formatted date"""

    photo = get_photo_by_id(photo_id)
    date_taken = photo.date_taken

    date = time.strftime("%Y-%b-%w")
    print(date)






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

