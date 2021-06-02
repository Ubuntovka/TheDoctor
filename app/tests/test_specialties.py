from app import app, models, db
from app.models import Doctor
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

    ########################
    #### helper methods ####
    ########################

    def add_specialties(self):
        sp1 = Doctor('Andrei', 'pediatrician', 'doctor', 5, b'photos_of_doctors/dr1.jpg')
        sp2 = Doctor('Misha', 'ophthalmologist', 'doctor', 10, b'photos_of_doctors/dr1.jpg')
        sp3 = Doctor('Nikolay', 'gynecologist', 'doctor', 12, b'photos_of_doctors/dr1.jpg')
        sp4 = Doctor('Stephan', 'gastroenterologist', 'doctor', 1, b'photos_of_doctors/dr1.jpg')
        db.session.add(sp1)
        db.session.add(sp2)
        db.session.add(sp3)
        db.session.add(sp4)
        db.session.commit()

    ###############
    #### tests ####
    ###############

    def test_specialties_sort_key(self):
        self.add_specialties()
        response = self.app.get('/specialties/pediatrician', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Specialty:<br>pediatrician', response.data)
        self.assertNotIn(b'Specialty:<br>ophthalmologist', response.data)
        self.assertNotIn(b'Specialty:<br>gynecologist', response.data)
        self.assertNotIn(b'Specialty:<br>gastroenterologist', response.data)

        response = self.app.get('/specialties/ophthalmologist', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Specialty:<br>ophthalmologist', response.data)
        self.assertNotIn(b'Specialty:<br>pediatrician', response.data)
        self.assertNotIn(b'Specialty:<br>gynecologist', response.data)
        self.assertNotIn(b'Specialty:<br>gastroenterologist', response.data)

        response = self.app.get('/specialties/gynecologist', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Specialty:<br>gynecologist', response.data)
        self.assertNotIn(b'Specialty:<br>pediatrician', response.data)
        self.assertNotIn(b'Specialty:<br>ophthalmologist', response.data)
        self.assertNotIn(b'Specialty:<br>gastroenterologist', response.data)

        response = self.app.get('/specialties/gastroenterologist', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Specialty:<br>gastroenterologist', response.data)
        self.assertNotIn(b'Specialty:<br>pediatrician', response.data)
        self.assertNotIn(b'Specialty:<br>ophthalmologist', response.data)
        self.assertNotIn(b'Specialty:<br>gynecologist', response.data)

    def test_specialties_valid_id(self):
        self.add_specialties()
        response = self.app.get('/specialties/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Andrei', response.data)
        self.assertNotIn(b'Misha', response.data)
        self.assertNotIn(b'Nikolay', response.data)
        self.assertNotIn(b'Stephan', response.data)
        response = self.app.get('/specialties/2', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Misha', response.data)
        self.assertNotIn(b'Andrei', response.data)
        self.assertNotIn(b'Nikolay', response.data)
        self.assertNotIn(b'Stephan', response.data)
        response = self.app.get('/specialties/3', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Nikolay', response.data)
        self.assertNotIn(b'Andrei', response.data)
        self.assertNotIn(b'Misha', response.data)
        self.assertNotIn(b'Stephan', response.data)
        response = self.app.get('/specialties/4', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Stephan', response.data)
        self.assertNotIn(b'Andrei', response.data)
        self.assertNotIn(b'Misha', response.data)
        self.assertNotIn(b'Nikolay', response.data)

    def test_specialties_invalid_id(self):
        self.add_specialties()
        response = self.app.get('/specialties/10', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
