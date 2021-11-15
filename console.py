import pdb
from models.pet import Pet
from models.vet import Vet 
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

vet_1 = Vet("Jane Doe")
vet_repository.save(vet_1)

pet_1 = Pet("Cali", "Sneddon", "Dog", "06/02/2021", "07382516823", vet_1)
pet_repository.save(pet_1)
pet_2 = Pet("Slinky", "Liston", "Cat", "26/06/2011", "07348959353", vet_1)
pet_repository.save(pet_2)
pet_3 = Pet("Max", "Walker", "Dog", "23/08/2009", "07924186275", vet_1)
pet_repository.save(pet_3)