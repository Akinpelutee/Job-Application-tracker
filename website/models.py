# from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "Database.db"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    #One to many relationship
    jobs = db.relationship("Job", backref="user", lazy=True)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(150), nullable=False)
    position = db.Column(db.String(150), nullable=False)
    application_date = db.Column(db.DateTime(timezone=True), default=func.now())
    status = db.Column(db.String(50), default='Applied')    #Interview, offer, rejected
    job_type = db.Column(db.String(50))     #Full time, part time, internship
    location = db.Column(db.String(100))
    link = db.Column(db.String(300))
    notes = db.Column(db.Text)
    #Foreign key to the user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
