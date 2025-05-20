from models import Building, TypeBuilding, Country, City
from config import db, ma

class TypeBuildingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TypeBuilding

class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Country

class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City
    country = ma.Nested(CountrySchema())

class BuildingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Building
        load_instance = True
        sqla_session = db.session
    type_building = ma.Nested(TypeBuildingSchema())
    city = ma.Nested(CitySchema())
    type_building_id = ma.auto_field()
    city_id = ma.auto_field()

building_schema = BuildingSchema()
buildings_schema = BuildingSchema(many=True)