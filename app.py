from flask import Flask, render_template, redirect, url_for
from models import db, connect_db, Pet, DEFAULT_IMAGE_URL
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:walmart48@localhost/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'somesecretkey'

connect_db(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def show_pets():
    """Show home page. List of pets"""

    pets = Pet.query.all()
    return render_template('pets_list.html', pets=pets)

@app.route('/add', methods=['GET'])
def add_pet_form():
    """Show add pet form"""

    form = AddPetForm()
    return render_template('add_pet_form.html', form=form)

@app.route('/add', methods=['POST'])
def add_pet():
    """Add pet to database"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # If no photo_url provided, use default
        if not photo_url:
            photo_url = DEFAULT_IMAGE_URL

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect(url_for('show_pets'))
    else:
        return render_template('add_pet_form.html', form=form)