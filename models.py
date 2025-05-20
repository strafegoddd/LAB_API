from config import db
from app import app

class TypeBuilding(db.Model):
   __tablename__ = 'type_building'

   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   type_name = db.Column('Тип', db.String(50), nullable=False)

   buildings = db.relationship(
       "Building",
       back_populates="type_building",
       cascade="all, delete",
       passive_deletes=True
   )

   def __init__(self, type_name):
      self.type_name = type_name

   def __repr__(self):
      return f'\nid: {self.id}, Тип: {self.type_name}'

class Country(db.Model):
   __tablename__ = 'country'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column('Страна', db.String(100), nullable=False)

   cities = db.relationship("City", back_populates="country")

   def __init__(self, name):
      self.name = name
   
   def __repr__(self):
      return f"id: {self.id}, Страна: {self.name}"


class City(db.Model):
   __tablename__ = 'city'
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name = db.Column('Город', db.String(100))

   country_id = db.Column(db.Integer, db.ForeignKey('country.id', ondelete='CASCADE'))
   country = db.relationship("Country", back_populates="cities", cascade="all, delete",  passive_deletes=True)

   buildings = db.relationship(
        "Building",
        back_populates="city",
        cascade="all, delete",
        passive_deletes=True
    )
   
   def __init__(self, name, country_id):
      self.name = name
      self.country_id = country_id

   def __repr__(self):
      return f"id: {self.id}, Город: {self.name}, country_id: {self.country_id}"

class Building(db.Model):
   __tablename__ = 'building'
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column('Название', db.String(200))
   type_building_id = db.Column(db.Integer, db.ForeignKey('type_building.id', ondelete='CASCADE'))
   city_id = db.Column(db.Integer, db.ForeignKey('city.id', ondelete='CASCADE'))
   year = db.Column(db.Integer)
   height = db.Column(db.Float)
   type_building = db.relationship("TypeBuilding", back_populates="buildings")
   city = db.relationship("City", back_populates="buildings")

   def __init__(self, title, type_building_id, city_id, year, height):
      self.title = title
      self.type_building_id = type_building_id
      self.city_id = city_id
      self.year = year
      self.height = height
   
   def __repr__(self):
      return (f"id: {self.id}, Здание: {self.title}, type_building_id: {self.type_building_id}, "
         f"city_id: {self.city_id}, Год: {self.year}, Высота: {self.height}")

app.app_context().push()
with app.app_context():
   db.create_all()