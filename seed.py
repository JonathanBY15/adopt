"""Seed the 'adopt' database with sample data.
Run this file to reset the database and create sample data."""

from app import app
from models import db, Pet, DEFAULT_IMAGE_URL

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

    # If tables aren't empty, empty them
    Pet.query.delete()

    # Add pets
    pet1 = Pet(name='Bella', species='Dog', photo_url=DEFAULT_IMAGE_URL, age=3, notes='Loves to play fetch.', available=True)
    pet2 = Pet(name='Max', species='Cat', photo_url=DEFAULT_IMAGE_URL, age=2, notes='Very friendly and playful.', available=True)
    pet3 = Pet(name='Charlie', species='Rabbit', photo_url=DEFAULT_IMAGE_URL, age=1, notes='Enjoys being petted.', available=False)
    pet4 = Pet(name='Lucy', species='Bird', photo_url=DEFAULT_IMAGE_URL, age=4, notes='Can mimic sounds.', available=True)

    db.session.add_all([pet1, pet2, pet3, pet4])
    db.session.commit()
