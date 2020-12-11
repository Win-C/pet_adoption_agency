"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Note to link this as a default image later
DEFAULT_IMAGE_URL = 'https://lh3.googleusercontent.com/proxy/0EAAzvBwIhh8pC4yWHlYXxpp21lEaAN51Jz7Z4exM6jFzVJ0J6V-I5W3h2-wFtG5phN2nQQlXJ3KPIEnh_gOcutF9hZ6qrI'


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ Create a pet. """

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
        )
    name = db.Column(
        db.Text,
        nullable=False
        )
    species = db.Column(
        db.Text,
        nullable=False
        )
    photo_url = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_IMAGE_URL
        )
    age = db.Column(
        db.Text,
        nullable=False
        )
    notes = db.Column(
        db.Text,
        nullable=False
        )
    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
        )

    def __repr__(self):

        return f'I"m a {self.species} and my name is {self.name}'
