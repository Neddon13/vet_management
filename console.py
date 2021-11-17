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
vet_3 = Vet("Jo Smith")
vet_repository.save(vet_3)

owner_1 = Owner("Joe King", "17 Howden Place", "07536294765")
owner_repository.save(owner_1)
owner_2 = Owner("Sam Johnson", "46 Craig Road", "07651001283")
owner_repository.save(owner_2)
owner_3 = Owner("Craig Miller", "88 North Street", "07776109821")
owner_repository.save(owner_3)
owner_4 = Owner("Luke Grant", "5 Queen Street", "07922415762")
owner_repository.save(owner_4)
owner_5 = Owner("Chris Sneddon", "62 Broadway Road", "07646839012")
owner_repository.save(owner_5)
owner_6 = Owner("Carol Liston", "30 Hallmark street", "07333620198")
owner_repository.save(owner_6)
owner_7 = Owner("Kelsey Walker", "8 Mount Green", "07902286473")
owner_repository.save(owner_7)



pet_1 = Pet("Cali", "Sneddon", "Dog", "06/02/2021", "second vaccination done", vet_1, owner_5)
pet_repository.save(pet_1)
pet_2 = Pet("Slinky", "Liston", "Cat", "26/06/2011", "minor injury to paw bandaged up", vet_3, owner_6)
pet_repository.save(pet_2)
pet_3 = Pet("Max", "Walker", "Dog", "23/08/2009", "neutering in progress", vet_2, owner_7)
pet_repository.save(pet_3)

pet_repository.select_all()
vet_repository.select_all()
owner_repository.select_all()

