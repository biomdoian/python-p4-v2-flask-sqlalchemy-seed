#!/usr/bin/env python3
#server/seed.py
from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():

    fake = Faker()

    Pet.query.delete() # Clear the Pet table before seeding

    # Create an empty list
    pets = []

    species = ["Dog", "Cat", "Hamster", "Chicken", "Turtule"]

    for n in range(10):
          pet = Pet(name=fake.first_name(), species=rc(species))
          pets.append(pet)

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()