from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.pet import Pet
from models.vet import Vet
from models.owner import Owner
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/register")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets = pets)

@pets_blueprint.route("/register/new", methods=["GET"])
def new_pet():
    vets    = vet_repository.select_all()
    owners  = owner_repository.select_all()
    return render_template("pets/new.html", vets=vets, owners=owners)

@pets_blueprint.route("/register",  methods=['POST'])
def create_pet():
    first_name      = request.form['FirstName']
    last_name       = request.form['LastName']
    type_of_pet     = request.form['TypeOfPet']
    date_of_birth   = request.form['DateOfBirth']
    vet_id          = request.form['vet_id']
    owner_id        = request.form['owner_id']
    vet             = vet_repository.select(vet_id)
    owner           = owner_repository.select(owner_id)
    pet             = Pet(first_name, last_name, type_of_pet, date_of_birth, vet, owner)
    pet_repository.save(pet)
    return redirect('/register')

@pets_blueprint.route("/register/<id>/delete", methods=['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/register')
