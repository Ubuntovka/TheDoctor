from datetime import datetime
from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(300), nullable=False)
    position = db.Column(db.String(300), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.LargeBinary)
    working_time = db.Column(db.String(100))

    def __repr__(self):
        return '<Doctor %r>' % self.id


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    doctor = db.relationship('Doctor', backref=db.backref('records', lazy=True))

    def __repr__(self):
        return '<Record %r>' % self.id
