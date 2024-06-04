from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet Name")
    species = StringField("Species", validators=[InputRequired(), AnyOf(['dog', 'cat', 'porcupine'], message="Species must be dog, cat, or porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")
    available = BooleanField("Available")