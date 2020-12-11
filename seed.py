"""Seed file to make sample data for adopt db."""

from models import db, connect_db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
pet1 = Pet(
    name="Woofly",
    species="dog",
    photo_url="https://i.pinimg.com/originals/30/6a/7e/306a7ee9b017127f3c36d793d7cfbd6f.jpg",
    age=1,
    notes='young',
    available=True
    )
pet2 = Pet(
    name="Porchetta",
    species="porcupine",
    photo_url="https://s26961.pcdn.co/wp-content/uploads/sites/3/2018/12/quillbur.jpg",
    age=2,
    notes='adult',
    available=False
    )
pet3 = Pet(
    name="Snargle",
    species="cat",
    photo_url="https://images.unsplash.com/photo-1572590407445-ac6252f1a5b1?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxleHBsb3JlLWZlZWR8M3x8fGVufDB8fHw%3D&w=1000&q=80",
    age='',
    notes='senior',
    available=True
    )

# Add new objects to session, so they'll persist
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)

# Commit--otherwise, this never gets saved!
db.session.commit()
