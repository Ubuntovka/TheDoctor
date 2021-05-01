from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import classes_for_models
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mariia:root@localhost/clinic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


db.create_all()


@app.route('/')
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/posts")
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
