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

    # def test_library_page(self):
    #     """Test library page"""

    #     result = self.client.get("/library")
    #     # self.assertIn(b"Library", result.data)

    def test_photo_details(self):
        """Test photo detail page"""

        result = self.client.get("/1")
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

        photo = crud.create_photo(1,date_uploaded, date_taken, 1, "/static/img/co1.jpg")

        assert photo.user_id == 1
        self.assertEqual(photo.date_uploaded, date_uploaded)
        self.assertEqual(photo.date_taken, date_taken)
        assert photo.album_id == 1
        assert photo.path == "/static/img/co1.jpg"


    def test_create_album(self):   
        date_created = datetime.now()
        
        album = crud.create_album('Album', date_created)
        assert album.name == 'Album'
        self.assertEqual(album.date_created, date_created)


    def test_get_photos_by_album_id(self):
        photos = crud.get_photos_by_album_id(1)
        assert photos[0].album_id == 1


    def test_get_photo_by_id(self):
        photo = crud.get_photo_by_id(1)

        assert photo.photo_id == 1

    
    def test_get_album_by_id(self):
        album = crud.get_album_by_id(1)

        assert album.album_id == 1


    def test_get_user_by_email(self):
        email = 'user1@user.com'
        user = crud.get_user_by_email(email)

        self.assertEqual (user.email, email)

    
    def test_get_id_by_email(self):
        email = 'user1@user.com'
        user_id = crud.get_id_by_email(email)
        user = crud.get_user_by_email(email)

        self.assertEqual(user_id, user.user_id)
        
    
    def test_check_password(self):
        email = 'user1@user.com'
        password = '123'
        check = crud.check_password(email, password)
        user = crud.get_user_by_email(email)

        self.assertEqual(password, user.password)


    def test_give_rating(self):
        photo_id = 1
        photo = crud.get_photo_by_id(photo_id)
        crud.give_rating(photo_id,7)
        self.assertEqual(photo.rating , 7)
        crud.give_rating(photo_id,4)
        self.assertEqual(photo.rating, 4)
        

    def test_get_album_by_name(self):
        name = 'Album1'
        album = crud.get_album_by_name(name)
        self.assertEqual(album.name, name)

    
    def test_display_photoalbum(self):
        album_id = 1
        photoalbum = crud.display_photoalbum(album_id)
        self.assertEqual(photoalbum[0].album_id, album_id)

# TODO when I have a working session
# class FlaskTestsLoggedIn(TestCase):
#     """Flask tests with user logged in to session."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         app.config['TESTING'] = True
#         app.config['SECRET_KEY'] = 'key'
#         self.client = app.test_client()

#         with self.client as c:
#             with c.session_transaction() as sess:
#                 sess['user_id'] = 1

#     def test_important_page(self):
#         """Test important page."""

#         result = self.client.get("/important")
#         self.assertIn(b"You are a valued user", result.data)


# class FlaskTestsLoggedOut(TestCase):
#     """Flask tests with user logged in to session."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         app.config['TESTING'] = True
#         self.client = app.test_client()

#     def test_important_page(self):
#         """Test that user can't see important page when logged out."""

#         result = self.client.get("/important", follow_redirects=True)
#         self.assertNotIn(b"You are a valued user", result.data)
#         self.assertIn(b"You must be logged in", result.data)


# class FlaskTestsLogInLogOut(TestCase):  # Bonus example. Not in lecture.
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
