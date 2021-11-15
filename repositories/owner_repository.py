from db.run_sql import run_sql
from models.owner import Owner


def save(owner):
    sql = "INSERT INTO owners (name, address, mobile_num) VALUES (%s, %s, %s) RETURNING *"
    values = [owner.name, owner.address, owner.mobile_num]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = Owner(result['name'], result['address'], result['mobile_num'], result['id'])
    return owner










# def select_all():
#     owners = []

#     sql = "SELECT * FROM owners"
#     results = run_sql(sql)

#     for row in results:
#         owner = Owner(row['name'], row['address'], row['mobile_num'], row['id'])
#         owners.append(owner)
#     return owner