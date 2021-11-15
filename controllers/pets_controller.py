from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/register")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets = pets)

@pets_blueprint.route("/register/new", methods=["GET"])
def new_pet():
    return render_template("pets/new.html")

@pets_blueprint.route("/register",  methods=['POST'])
def create_pet():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    type_of_pet = request.form['type_of_pet']
    date_of_birth = request.form['date_of_birth']
    vet = request.form['vet']
    owner = request.form['owner']


