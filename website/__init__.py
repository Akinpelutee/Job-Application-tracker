from flask import Flask,flash
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .job import JobResource, job_bp
from .views import views
from .auth import auth
from .dashboard import dashboard
from flask_login import LoginManager
from os import path
from .models import db
import os
from dotenv import load_dotenv

load_dotenv()

# db = SQLAlchemy()
DB_NAME = "Database.db"

def create_app():
    app = Flask(__name__)
    api = Api(app)
    SECRET_KEY = os.getenv("SECRET_KEY")
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(dashboard, url_prefix="/")
    #app.register_blueprint(job_bp, url_prefix="/")


    #Register api route
    api.add_resource(JobResource, "/job", "/job/<int:id>")

    # login_manager = LoginManager()
    # login_manager.login_view = "auth.login"
    # login_manager.init_app(app)

    from .models import User,Job
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app, api

def create_database(app):
    if not path.exists('website/,' + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Created Database!")
