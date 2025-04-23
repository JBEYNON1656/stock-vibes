from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StockNews(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	symbol = db.Column(db.String(10), nullable=False)
	title = db.Column(db.String(255))
	description = db.Column(db.Text)
	published_at = db.Column(db.String(50))
	sentiment = db.Column(db.String(20))
	timestamp = db.Column(db.String(50))   