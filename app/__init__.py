from flask import Flask #imports the Flask class from the flask package
from .routes import bp #imports bp variable from routes.py in this dir

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app