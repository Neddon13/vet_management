from db.run_sql import run_sql
from models.owner import Owner


def save(owner):
    sql = "INSERT INTO owners (name, address, mobile_num) VALUES (%s, %s, %s) RETURNING *"
    values = [owner.name, owner.address, owner.mobile_num]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner