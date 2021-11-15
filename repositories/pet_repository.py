from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet
from models.owner import Owner 
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository


def save(pet):
    sql = f"INSERT INTO pets (first_name, last_name, type_of_pet, date_of_birth, vet_id, owner_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.first_name, pet.last_name, pet.type_of_pet, pet.date_of_birth, pet.vet.id, pet.owner.id]
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
        pet = Pet(row['first_name'], row['last_name'], row['type_of_pet'], row['date_of_birth'], vet, owner, row['id'])
        pets.append(pet)
    return pets