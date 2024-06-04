from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://st3.depositphotos.com/18509294/34839/v/450/depositphotos_348397686-stock-illustration-pet-lovers-logo-inspirations-lovely.jpg"

class Pet(db.Model):
    """Pet."""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default=DEFAULT_IMAGE_URL)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

def connect_db(app):
    """Connect db to flask."""

    db.app = app
    db.init_app(app)