from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet
from models.owner import Owner 
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository


def save(pet):
    sql = f"INSERT INTO pets (first_name, last_name, type_of_pet, date_of_birth, treatment_notes, vet_id, owner_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.first_name, pet.last_name, pet.type_of_pet, pet.date_of_birth, pet.treatment_notes, pet.vet.id, pet.owner.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet 

def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql) 

    for row in results:
        vet = vet_repository.select(row['vet_id']) 
        owner = owner_repository.select(row['owner_id'])
        pet = Pet(row['first_name'], row['last_name'], row['type_of_pet'], row['date_of_birth'], row['treatment_notes'], vet, owner, row['id'])
        pets.append(pet)
    return pets

def select(id): 
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]


    vet = vet_repository.select(result['vet_id'])
    owner = owner_repository.select(result['owner_id'])
    pet = Pet(result['first_name'], result['last_name'], result['type_of_pet'], result['date_of_birth'], result['treatment_notes'], vet, owner, result['id'])
    return pet

def delete(id):
    sql = "DELETE  FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(pet):
    sql = "UPDATE pets SET (first_name, last_name, type_of_pet, date_of_birth, treatment_notes, vet_id, owner_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.first_name, pet.last_name, pet.type_of_pet, pet.date_of_birth, pet.treatment_notes, pet.vet.id, pet.owner.id, pet.id]
    run_sql(sql, values)