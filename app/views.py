from flask import render_template, request, redirect, jsonify, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField

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
    article = models.Article.query.get(id)
    return render_template("post_detail.html", article=article)


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
    doctor = models.Doctor.query.get(id)
    return render_template("doctor_detail.html", doctor=doctor)


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
        the_doctor = models.Doctor.query.filter_by(fio=form.doctor.data).first()
        doctor_id = the_doctor.id

        new_record = models.Record(name=name, phone_number=phone_number, email=email, doctor_id=doctor_id)

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
