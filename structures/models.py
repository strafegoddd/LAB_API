from models import Building
from config import db
from structures.serializers import building_schema
from sqlalchemy import func

def get_all_buildings():
    query = Building.query.all()
    return query

def get_building(building_id):
    query = Building.query.filter(Building.id == building_id).one_or_none()
    return query

def insert_building(new_building):
    item = building_schema.load(new_building, session=db.session)
    db.session.add(item)
    db.session.commit()
    # возвращаем вставленную запись, то есть запись с максимальным id
    return Building.query.\
    filter(Building.id == db.session.query(func.max(Building.id))).\
    one_or_none()

def update_building(building_id, update_par):
    Building.query.filter(Building.id == building_id).update(update_par)
    db.session.commit()
    building = get_building(building_id)
    return building

def delete_building(building_id):
    building = get_building(building_id)
    if building:
        db.session.delete(building)
        db.session.commit()
        return True
    return False
