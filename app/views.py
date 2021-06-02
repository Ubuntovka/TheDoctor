from flask import render_template, request, redirect, jsonify, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SelectField
from email_validator import validate_email, EmailNotValidError
import re

from app import app, models, db


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    articles = models.Article.query.order_by(models.Article.date.desc()).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:id>')
def post_detail(id):
    article = models.Article.query.filter_by(id=id).first_or_404()
    return render_template("post_detail.html", article=article)


@app.route('/posts/<int:id>/del')
def post_delete(id):
    article = models.Article.query.get_or_404(id)
    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return "An error occurred while deleting the article."


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = models.Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "An error occurred while editing the article."
    else:
        return render_template("post_update.html", article=article)


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = models.Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return "An error occurred while adding an article."
    else:
        return render_template("create-article.html")


@app.route('/price')
def price():
    return render_template('price.html')


@app.route('/specialties')
@app.route('/specialties/<sort_key>')
def specialties(sort_key=None):
    if sort_key is not None:
        doctors = models.Doctor.query.where(models.Doctor.specialty == sort_key).all()
    else:
        doctors = models.Doctor.query.all()
    return render_template('specialties.html', doctors=doctors)


@app.route('/specialties/<int:id>')
def doctor_detail(id):
    doctor = models.Doctor.query.filter_by(id=id).first_or_404()
    return render_template("doctor_detail.html", doctor=doctor)


@app.route('/about')
def about():
    return render_template('about.html')


# Dependence of the doctor on the specialty in the application for an appointment!
class Form(FlaskForm):
    specialty = SelectField('specialty',
                            choices=['gynecologist', 'pediatrician', 'ophthalmologist', 'gastroenterologist'])
    doctor = SelectField('doctor', choices=[])


@app.route('/application', methods=['GET', 'POST'])
def record():
    form = Form()
    form.doctor.choices = [(el.id, el.fio) for el in models.Doctor.query.filter_by(specialty='gynecologist').all()]

    if request.method == "POST":
        name = request.form['name']
        phone_number = request.form['phone_number']
        email = request.form['email']

        if len(name) > 100 or len(name) == 0:
            flash('Enter a name between 0 and 100 characters.')

        if not re.match(r'\+[3][8][0]\d{8}', phone_number) or not len(phone_number) == 13:
            phone_number_error = 'Enter a valid phone number. Format: +380123456789.'
            flash('The phone number is not valid.')
            return render_template('application.html', form=form, phone_number_error=phone_number_error)

        try:
            # Validate.
            valid = validate_email(email)

            # Update with the normalized form.
            email = valid.email
        except EmailNotValidError as e:
            email_error = str(e)
            flash('The email is not valid.')
            return render_template('application.html', form=form, email_error=email_error)
        if form.doctor.data:
            the_doctor = models.Doctor.query.filter_by(fio=form.doctor.data).first()
            doctor_id = the_doctor.id
            new_record = models.Record(name=name, phone_number=phone_number, email=email, doctor_id=doctor_id)
        else:
            new_record = models.Record(name=name, phone_number=phone_number, email=email)

        try:
            db.session.add(new_record)
            db.session.commit()
            return redirect('/')
        except:
            return "An error occurred while adding an application."
    return render_template('application.html', form=form)


@app.route('/application/doctor/<specialty>')
def doctor(specialty):
    doctors = models.Doctor.query.filter_by(specialty=specialty).all()

    list_of_doctors = []

    for one_doc in doctors:
        doctor_obj = {'id': one_doc.id, 'fio': one_doc.fio}
        list_of_doctors.append(doctor_obj)

    return jsonify({'doctors': list_of_doctors})

# END
