# TheDoctor

## Description
This project provides an opportunity for clients of the clinic to familiarize themselves with the list of
services / specialists provided and apply for an appointment. You can also read the news.

## How to Run (Development)
1. To install all required dependencies(Make sure you have pip installed!):
* ~$ pip install -r requirements.txt

2. Database Setup:
* In the TheDoctor/app/\_\_init__.py file, on the sixth line, change the line after the equal sign to the one that will match 
  your database settings.
* <https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format>  

3. Create the database:
* ~$ TheDoctor/instance/db_create.py

4. We launch the project locally:
* ~$ TheDoctor/start.py

Go to your favorite web browser and open: http://127.0.0.1:5000/

## Key Python Modules Used
* Flask - web framework
* Jinga2 - templating engine
* SQLAlchemy - ORM (Object Relational Mapper)
* Flask-Migrate - database migrations
* Flask-WTF - simplifies forms
* itsdangerous - helps with user management, especially tokens

This application is written using Python 3.9.  The database used is PostgreSQL.

## Contributing
The project is under development, it is planned to add user registration, reviews, fill in blank pages, and more.
