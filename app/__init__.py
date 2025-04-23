from flask import Flask #imports the Flask class from the flask package
from .routes import bp #imports bp variable from routes.py in this dir
from app.models import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stockvibes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
		
    return app