from app import app, models, db
from app.models import Article
import unittest

TEST_DB = 'test.db'


class ClinicArticlesTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['LOGIN_DISABLED'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        self.app = app.test_client()
        models.db.drop_all()
        models.db.create_all()

    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    ########################
    #### helper methods ####
    ########################

    def add_articles(self):
        at1 = Article('some title for at1', 'some intro for at1', 'some text for at1')
        at2 = Article('some title for at2', 'some intro for at2', 'some text for at2')
        db.session.add(at1)
        db.session.add(at2)
        db.session.commit()

    ###############
    #### tests ####
    ###############

    def test_posts_valid_id(self):
        self.add_articles()
        response = self.app.get('/posts/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'some title for at1', response.data)
        self.assertNotIn(b'some title for at2', response.data)

        response = self.app.get('/posts/2', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'some title for at2', response.data)
        self.assertNotIn(b'some title for at1', response.data)

    def test_posts_invalid_id(self):
        self.add_articles()
        response = self.app.get('/posts/52', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_posts_delete(self):
        self.add_articles()
        response = self.app.get('/posts/1/del', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'some title for at2', response.data)
        self.assertNotIn(b'some title for at1', response.data)
