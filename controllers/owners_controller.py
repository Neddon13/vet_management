from flask import Flask, render_template, redirect, request
from flask import Blueprint
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository
from models.owner import Owner 


owners_blueprint = Blueprint("owners", __name__)


@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", owners = owners)

@owners_blueprint.route("/owners/new", methods=["GET"])
def new_owner():
    owner = owner_repository.select_all()
    return render_template("owners/new.html", owner=owner)

@owners_blueprint.route("/owners",  methods=['POST'])
def create_owner():
    name        = request.form['Name']
    address     = request.form['Address']
    mobile_num  = request.form['MobileNum']
    owner       = Owner(name, address, mobile_num)
    owner_repository.save(owner)
    return redirect('/owners')

@owners_blueprint.route("/owners/<id>", methods=['GET'])
def show_owner(id):
    owner = owner_repository.select(id) 
    return render_template('owners/show.html', owner = owner)

@owners_blueprint.route("/owners/<id>/edit", methods=['GET'])
def edit_owner_form(id):
    owners = owner_repository.select(id)
    return render_template('owners/edit.html', owners = owners)

@owners_blueprint.route("/owners/<id>/edit",  methods=['POST'])
def update_owner():
    name        = request.form['Name']
    address     = request.form['Address']
    mobile_num  = request.form['MobileNum']
    owner       = Owner(name, address, mobile_num)
    owner_repository.update(owner)  
    return redirect('/owners')

@owners_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect('/owners')