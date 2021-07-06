from datetime import datetime

from flask_login import UserMixin

from app import db, manager


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title=None, intro=None, text=None, date=None):
        self.title = title
        self.intro = intro
        self.text = text
        self.date = date

    def __repr__(self):
        return '<Article %r>' % self.id


class Doctor(db.Model):
    __tablename__ = 'doctor'

    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(300), nullable=False)
    position = db.Column(db.String(300), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.LargeBinary)
    working_time = db.Column(db.String(100))

    def __init__(self, fio=None, specialty=None, position=None, experience=None, photo=None, working_time=None):
        self.fio = fio
        self.specialty = specialty
        self.position = position
        self.experience = experience
        self.photo = photo
        self.working_time = working_time

    def __repr__(self):
        return '<Doctor %r>' % self.id


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    doctor = db.relationship('Doctor', backref=db.backref('records', lazy=True))

    def __repr__(self):
        return '<Record %r>' % self.id


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    phone_number = db.Column(db.String(100), nullable=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

