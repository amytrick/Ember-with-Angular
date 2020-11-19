# import unittest
# import crud
# from model import connect_to_db
# from server import app

# class FlaskTests(TestCase):



#     def setUp(self):
#         """Tasks to run before each test is run"""

#         # Get the Flask test client
#         self.client = app.client()
#         app.config['TESTING'] = True

#         # Connect to test database
#         connect_to_db(app, "postgresql:///testdb")

#         # Create tables and add sample data
#         db.create_all()

#     def tearDown(self):

# # This was my first class before following Flask Testing notes
# # class CrudTester(unittest.TestCase):

#     def test_create_user(self):
#         user = crud.create_user('Testy', 'Testerson', 'ttesterson@test.com', '123')
#         assert user.fname == 'Testy'
#         assert user.lname == 'Testerson'
#         assert user.email == 'ttesterson@test.com'
#         assert user.password == '123'

# if __name__== '__main__':
#     from server import app
#     connect_to_db(app)
#     unittest.main()

################################################################

from unittest import TestCase
import unittest
from datetime import datetime

from server import app
from model import connect_to_db, db, example_data
import crud
# from flask import session


# class FlaskTestsBasic(TestCase):
#     """Flask tests."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         # Get the Flask test client
#         self.client = app.test_client()

#         # Show Flask errors that happen during tests
#         app.config['TESTING'] = True

#     def test_index(self):
#         """Test homepage page."""

#         result = self.client.get("/")
#         self.assertIn(b"<h1>Landing Page</h1>", result.data)

#     def test_login(self):
#         """Test login page."""

#         result = self.client.post("/login",
#                                   data={"email": "user1@user.com", "password": "123"},
#                                   follow_redirects=True)
#         self.assertIn(b"Library", result.data)


class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb", False)

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    def test_create_landingpage(self):
        """Test landing/login page"""

        result = self.client.get("/")
        self.assertIn(b"First name", result.data)

    def test_library_page(self):
        """Test library page"""

        result = self.client.get("/library")
        self.assertIn(b"Library", result.data)

    def test_photo_details(self):
        """Test photo detail page"""

        result = self.client.get("/photodetails/1")
        self.assertIn(b"Rating", result.data)

    def test_album_details(self):
        """Test album detail page."""

        result = self.client.get("/library/1")
        self.assertIn(b"Album :", result.data)

class CrudTester(unittest.TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb", False)

        # Create tables and add sample data
        db.drop_all()
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    def test_create_user(self):
        user = crud.create_user('Testy', 'Testerson', 'ttesterson@test.com', '123')

        assert user.fname == 'Testy'
        assert user.lname == 'Testerson'
        assert user.email == 'ttesterson@test.com'
        assert user.password == '123'

    def test_create_photo(self):
        date_taken = datetime.now()
        date_uploaded = datetime.now()

        photo = crud.create_photo(1, date_uploaded, date_taken, 1, "/static/img/co1.jpg")

        assert photo.user_id == 1
        self.assertEqual(photo.date_uploaded, date_uploaded)
        self.assertEqual(photo.date_taken, date_taken)
        assert photo.album_id == 1
        assert photo.path == "/static/img/co1.jpg"

    def test_create_album(self):
        date_created = datetime.now()
        user_id = 1

        album = crud.create_album('Album', date_created, user_id)
        assert album.name == 'Album'
        self.assertEqual(album.date_created, date_created)
        assert album.user_id == 1

    # def test_get_photos_by_album_id(self):
    #     photos = crud.get_photos_by_album_id(1)
    #     assert photos[0].album_id == 1

    def test_get_photo_by_id(self):
        photo = crud.get_photo_by_id(1)

        assert photo.photo_id == 1

    def test_get_album_by_id(self):
        album = crud.get_album_by_id(1)

        assert album.album_id == 1

    def test_get_user_by_email(self):
        email = 'user1@user.com'
        user = crud.get_user_by_email(email)

        self.assertEqual(user.email, email)

    def test_get_id_by_email(self):
        email = 'user1@user.com'
        user_id = crud.get_id_by_email(email)
        user = crud.get_user_by_email(email)

        self.assertEqual(user_id, user.user_id)

    def test_check_password(self):
        email = 'user1@user.com'
        password = '123'
        user = crud.get_user_by_email(email)

        self.assertEqual(password, user.password)

    def test_give_rating(self):
        photo_id = 1
        photo = crud.get_photo_by_id(photo_id)
        crud.give_rating(photo_id, 7)
        self.assertEqual(photo.rating, 7)
        crud.give_rating(photo_id, 4)
        self.assertEqual(photo.rating, 4)

    def test_get_album_by_name(self):
        name = 'Album1'
        album = crud.get_album_by_name(name)
        self.assertEqual(album.name, name)

    def test_add_to_photoalbum(self):
        photo_id = 1
        album_id = 1
        photoalbum = crud.add_to_photoalbum(photo_id, album_id)
        self.assertEqual(photoalbum.photo_id, photo_id)
        self.assertEqual(photoalbum.album_id, album_id)

    # def test_display_photoalbum(self):
    #     album_id = 1
    #     photoalbum = crud.display_photoalbum(album_id)
    #     self.assertEqual(photoalbum[0].album_id, album_id)

    def test_get_photos_by_user_id(self):
        user_id = 1
        photos = crud.get_photos_by_user_id(user_id)
        self.assertEqual(photos[0].user_id, user_id)

    def test_get_albums_by_user_id(self):
        user_id = 1
        albums = crud.get_albums_by_user_id(user_id)
        for album in albums:
            self.assertEqual(album.user_id, user_id)

    def test_get_user_by_user_id(self):
        user_id = 1
        user = crud.get_user_by_user_id(user_id)
        self.assertEqual(user.user_id, user_id)

    def test_add_to_phototags(self):
        photo_id = 1
        tag_id = 1
        phototag = crud.add_to_phototags(photo_id, tag_id)
        self.assertEqual(phototag.photo_id, photo_id)
        self.assertEqual(phototag.tag_id, tag_id)

    def test_get_tag_by_id(self):
        tag_id = 1
        tag = crud.get_tag_by_id(tag_id)
        self.assertEqual(tag.tag_id, tag_id)

    def test_create_tag(self):
        tagword = ('Tag3')
        tag = crud.create_tag(tagword)
        self.assertEqual(tagword, tag.tagword)

    def test_get_tag_by_tagword(self):
        tagword = 'Tag1'
        tag = crud.get_tag_by_tagword(tagword)
        self.assertEqual(tag.tagword, tagword)

    # def test_display_tags_by_photo_id(self):
    #     photo_id = 1
    #     tags = crud.display_tags_by_photo_id(photo_id)
    #     self.assertEqual(tags[0].photo_id, 1)
            # 'Tag' object has no attribute 'photo_id'

    def test_tag_exists(self):
        tagword = 'Tag1'
        self.assertTrue(crud.tag_exists(tagword))

    def test_get_photos_by_tag(self):
        tag = crud.get_tag_by_id(1)
        user_id = 1
        photos = crud.get_photos_by_tag(tag, user_id)
        # self.assertEqual(photos.tag.tag_id, tag.tag_id)
        self.assertEqual(photos[0].user_id, user_id)

    def test_get_photos_by_exact_rating(self):
        rating = 1
        photos = crud.get_photos_by_exact_rating(rating)
        self.assertEqual(photos[0].rating, rating)

    def test_get_photos_with_greater_or_equal_rating(self):
        rating = 1
        greater_rating = 2
        photos = crud.get_photos_with_greater_or_equal_rating(rating)
        self.assertEqual(photos[1].rating, greater_rating)

    def test_get_photos_with_less_or_equal_rating(self):
        rating = 2
        lesser_rating = 1
        photos = crud.get_photos_with_less_or_equal_rating(rating)
        self.assertEqual(photos[0].rating, lesser_rating)

    def test_get_phototag_record(self):
        photo_id = 1
        tag_id = 1
        phototag = crud.get_phototag_record(photo_id, tag_id)
        self.assertEqual(phototag.photo_id, photo_id)
        self.assertEqual(phototag.tag_id, tag_id)

    def test_remove_tag(self):
        tagword = 'Tag1'
        photo_id = 1
        crud.remove_tag(tagword, photo_id)
        tag = crud.get_tag_by_tagword(tagword)
        user_id = 1
        photos = crud.get_photos_by_tag(tag, user_id)
        photo = crud.get_photo_by_id(photo_id)
        self.assertNotIn(photo, photos)

    def test_remove_photo_from_album(self):
        photo_id = 1
        album_id = 1
        crud.remove_photo_from_album(photo_id, album_id)
        photo = crud.get_photo_by_id(photo_id)
        album = crud.get_album_by_id(album_id)
        photos = album.photos
        self.assertNotIn(photo, photos)

    def test_rename_album(self):
        album_id = 1
        new_name = 'NewAlbum'
        album = crud.rename_album(album_id, new_name)
        self.assertEqual(album.name, new_name)

class FlaskTestsLoggedIn(TestCase):
    """Flask tests with user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()
        app.config['TESTING'] = True


        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

        connect_to_db(app, "postgresql:///testdb")

        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_library_page(self):
        """Test library page."""

        result = self.client.get("/library")
        self.assertIn(b"Library", result.data)


# class FlaskTestsLogInLogOut(TestCase):
#     """Test log in and log out."""

#     def setUp(self):
#         """Before every test"""

#         app.config['TESTING'] = True
#         self.client = app.test_client()

#     def test_login(self):
#         """Test log in form.

#         Unlike login test above, 'with' is necessary here in order to refer to session.
#         """

#         with self.client as c:
#             result = c.post('/login',
#                             data={'user_id': '42', 'password': 'abc'},
#                             follow_redirects=True
#                             )
#             self.assertEqual(session['user_id'], '42')
#             self.assertIn(b"You are a valued user", result.data)

    # def test_logout(self):
    #     """Test logout route."""

    #     with self.client as c:
    #         with c.session_transaction() as sess:
    #             sess['user_id'] = '42'

    #         result = self.client.get('/logout', follow_redirects=True)

    #         self.assertNotIn(b'user_id', session)
    #         self.assertIn(b'Logged Out', result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()
