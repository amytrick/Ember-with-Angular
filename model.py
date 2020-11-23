"""Models for photo management app"""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(20))

    photo = db.relationship('Photo')
    album = db.relationship('Album')

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
        #currently not used
    tags = db.Column(db.Boolean)
        #currently not used
    path = db.Column(db.String)
    size = db.Column(db.Integer)
        #currently not used
    rating = db.Column(db.Integer)
    public_id = db.Column(db.String(50))

    user = db.relationship('User')
    albums = db.relationship('Album', secondary='photoalbums')
    tags = db.relationship('Tag', secondary='phototags')

    def __repr__(self):
        return f"<Photo photo_id = {self.photo_id}>"


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

    photos = db.relationship('Photo', secondary='phototags')

    def repr(self):
        return f"<Tag tag_id = {self.tag_id} tagword = {self.tagword}>"


class Photoalbum(db.Model):
    """A photoalbum - middle table between photos and albums"""

    __tablename__ = "photoalbums"

    photoalbum_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    photo_id = db.Column(db.Integer, db.ForeignKey("photos.photo_id"), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.album_id"), nullable=False)

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
        #currently not used
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    photos = db.relationship('Photo', secondary='photoalbums')
    users = db.relationship('User')

    def repr(self):
        return f"<Album album_id = {self.album_id} name = {self.name}>"


def example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    Photoalbum.query.delete()
    Phototag.query.delete()
    Photo.query.delete()
    Tag.query.delete()
    Album.query.delete()
    User.query.delete()

    # Add sample users, photos, and albums
    u1 = User(fname='User1', lname='User1', email='user1@user.com', password='123')
    u2 = User(fname='User2', lname='User2', email='user2@user.com', password='123')

    db.session.add_all([u1, u2])
    db.session.commit()

    a1 = Album(name='Album1', user_id=1)
    a2 = Album(name='Album2', user_id=2)

    db.session.add_all([a1, a2])
    db.session.commit()

    p1 = Photo(user_id=1, album_id=1, rating=1, path="/static/img/co1.jpg")
    p2 = Photo(user_id=2, album_id=2, rating=2, path="/static/img/co2.jpg")

    db.session.add_all([p1, p2])
    db.session.commit()

    pa1 = Photoalbum(photo_id=1, album_id=1)
    pa2 = Photoalbum(photo_id=2, album_id=2)

    db.session.add_all([pa1, pa2])
    db.session.commit()

    t1 = Tag(tagword='Tag1')
    t2 = Tag(tagword='Tag2')

    db.session.add_all([t1, t2])
    db.session.commit()

    pt1 = Phototag(photo_id=1, tag_id=1)
    pt2 = Phototag(photo_id=2, tag_id=2)

    db.session.add_all([pt1, pt2])
    db.session.commit()


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