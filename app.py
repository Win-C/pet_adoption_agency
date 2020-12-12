"""Flask app for adopt app."""

from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from project_secrets import PETFINDER_API_KEY, PETFINDER_API_SECRET
from forms import PetAddForm, PetEditForm
from petfinder_requests import get_oauth_token

import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

auth_token = None

@app.route("/")
def homepage():
    """ Show homepage links. """

    pets = Pet.query.all()

    return render_template("index.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def pet_add_form():
    """ Show the add form for a new pet. """

    form = PetAddForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        flash(f"Added a {species} called {name}")

        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url if photo_url != '' else None,
            age=age,
            notes=notes
        )

        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("pet_add_form.html", form=form)

        

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def pet_detail_edit(pet_id):
    """Show pet detail, edit form and handle edit."""

    pet = Pet.query.get_or_404(pet_id)
    form = PetEditForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"Pet{pet_id} updated!")
        return redirect(f"/{pet_id}")

    else:
        return render_template("pet_detail.html", form=form, pet=pet)


@app.before_first_request
def refresh_credentials():
    """Just once, get token and store it globally."""
    global auth_token
    auth_token = get_oauth_token()

