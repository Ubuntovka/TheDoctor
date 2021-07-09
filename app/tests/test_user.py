from werkzeug.security import generate_password_hash
from app import app, models, db
from app.models import Users
import unittest

TEST_DB = 'test.db'


class ClinicUserTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        self.app = app.test_client()
        models.db.drop_all()
        models.db.create_all()

    # executed after each test
    def tearDown(self):
        pass

    ########################
    #### helper methods ####
    ########################

    def add_users(self):
        usr1 = Users('Mariia', '+380562487598', 'asd@gmail.com', generate_password_hash('1234'))
        db.session.add(usr1)
        db.session.commit()

    ###############
    #### tests ####
    ###############

    def login(self, login, password):
        return self.app.post('/login', data=dict(
            login=login,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        self.add_users()
        rv = self.login('asd@gmail.com', '1234')
        self.assertIn(b'You were logged in', rv.data)
        rv = self.logout()
        self.assertIn(b'You were logged out', rv.data)

    def test_invalid_login(self):
        self.add_users()
        rv = self.login('asd@gmail', '1234')
        self.assertIn(b'Invalid login', rv.data)

    def test_invalid_password(self):
        self.add_users()
        rv = self.login('asd@gmail.com', '45897')
        self.assertIn(b'Invalid password', rv.data)
