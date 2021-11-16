from db.run_sql import run_sql
from models.vet import Vet

def save(vet):
    sql = "INSERT INTO vets (name) VALUES (%s) RETURNING *"
    values = [vet.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet


def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)
   

    for row in results:
        vet = Vet(row['name'], row['id'])
        vets.append(vet)
    return vets


def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = Vet(result['name'], result['id'])
    return vet

# def vets(vet):
#     vets = []

#     sql = "SELECT * FROM vets WHERE vet_id = %s"
#     values = [vet.id]
#     results = run_sql(sql, values)

#     for row in results:
#         vet = Vet(row['name'], row['vet_id'])
#         vets.append(vet)
#     return vets