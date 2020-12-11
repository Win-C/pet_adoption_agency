"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf, URL


class PetAddForm(FlaskForm):
    """ Form for adding pets. """

    name = StringField(
        "Name",
        validators=[InputRequired()]
        )
    species = StringField(
        "Species (dog, car, or porcupine)",
        validators=[InputRequired(),
                    AnyOf(['dog', 'cat', 'porcupine'])]
        )
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(),
                    URL()
                    ]
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


class PetEditForm(FlaskForm):
    """ Form for editing pet. """

    photo_url = StringField(
            "Photo URL",
            validators=[Optional(),
                        URL()
                        ]
            )
    notes = StringField(
        "Notes"
        )
    available = BooleanField(
        'Available'
    )