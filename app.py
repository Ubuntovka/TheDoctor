from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import session

from models import classes_for_models as models_class

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mariia:root@localhost/clinic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(300), nullable=False)
    position = db.Column(db.String(300), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.LargeBinary)

    def __repr__(self):
        return '<Doctor %r>' % self.id


db.create_all()


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    articles = models_class.Article.query.order_by(models_class.Article.date.desc()).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:id>')
def post_detail(id):
    article = models_class.Article.query.get(id)
    return render_template("post_detail.html", article=article)


@app.route('/specialties')
@app.route('/specialties/<sort_key>')
def specialties(sort_key=None):
    if sort_key is not None:
        doctors = Doctor.query.where(Doctor.specialty == sort_key).all()
    else:
        doctors = Doctor.query.all()
    return render_template('specialties.html', doctors=doctors)


@app.route('/specialties/<int:id>')
def doctor_detail(id):
    doctor = Doctor.query.get(id)
    return render_template("doctor_detail.html", doctor=doctor)


if __name__ == "__main__":
    app.run(debug=True)
