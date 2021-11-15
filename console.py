import pdb
from models.pet import Pet
from models.vet import Vet 
from models.owner import Owner
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

vet_1 = Vet("Jane Doe")
vet_repository.save(vet_1)
vet_2 = Vet("John Doe")
vet_repository.save(vet_2)
vet_3 = Vet("Hannah Smith")
vet_repository.save(vet_3)

owner_1 = Owner("Joe King", "17 Howden Place", "07536294765")
owner_repository.save(owner_1)
owner_2 = Owner("Sam Johnson", "46 Craig Road", "07651001283")
owner_repository.save(owner_2)


pet_1 = Pet("Cali", "Sneddon", "Dog", "06/02/2021", vet_1, owner_1)
pet_repository.save(pet_1)
pet_2 = Pet("Slinky", "Liston", "Cat", "26/06/2011", vet_3, owner_2)
pet_repository.save(pet_2)
pet_3 = Pet("Max", "Walker", "Dog", "23/08/2009", vet_2, owner_2)
pet_repository.save(pet_3)

