"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    """ Form for adding pets. """

    name = StringField(
        "Name",
        validators=[InputRequired()]
        )
    species = StringField(
        "Species",
        validators=[InputRequired()]
        )
    photo_url = StringField(
        "Photo URL"
        )
    age = SelectField(
        "Age",
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')
            ]
        )
    notes = StringField(
        "Notes"
        )
