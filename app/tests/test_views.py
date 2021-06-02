from app import app, models
import unittest

TEST_DB = 'test.db'


class ClinicFirstTest(unittest.TestCase):

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

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/home', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_application_page(self):
        response = self.app.get('/application', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_posts_page(self):
        response = self.app.get('/posts', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_specialties_page(self):
        response = self.app.get('/specialties', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_valid_application(self):
        response = self.application('Sam', '+380934025878', 'wildsam@gmail.com')
        self.assertEqual(response.status_code, 200)

    def test_invalid_application_email(self):
        response = self.application('Sam', '+380934025878', 'wildsam@kjhgvc.ijhg')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The email is not valid.', response.data)
        response = self.application('Sam', '+380934025878', '....@gmail.com')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The email is not valid.', response.data)

    def test_invalid_application_phone_number(self):
        response = self.application('Sam', '+38093402', 'wildsam@gmail.com')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The phone number is not valid.', response.data)
        response = self.application('Sam', '+38093402kg78', 'wildsam@kjhgvc.ijhg')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The phone number is not valid.', response.data)
        response = self.application('Sam', '5380934025878', 'wildsam@kjhgvc.ijhg')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The phone number is not valid.', response.data)

    def test_invalid_name(self):
        response = self.application(
            'Samkfghdjfhgnbkvghvhfdhfhljjjjjjjjjiiiiookokokogfrfgtrfgtredswerfgtyhjuytgfrvcgbnhgtfrdvcfghbgyhjnhgfvfgy',
            '+38093402', 'wildsam@gmail.com')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter a name between 0 and 100 characters.', response.data)

    ########################
    #### helper methods ####
    ########################

    def application(self, name, phone_number, email):
        return self.app.post(
            '/application',
            data=dict(name=name, phone_number=phone_number, email=email),
            follow_redirects=True
        )


if __name__ == '__main__':
    unittest.main()
