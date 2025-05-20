from flask_restful import Resource
from flask import jsonify, request, abort
from structures.models import get_all_buildings, get_building, insert_building, update_building, delete_building
from structures.serializers import buildings_schema, building_schema
from app import auth

class BuildingListAPI(Resource):
    @auth.login_required
    def get(self):
        buildings = get_all_buildings()
        return {"buildings": buildings_schema.dump(buildings)}

    @auth.login_required
    def post(self):
        if (not request.json
            or 'title' not in request.json
            or 'type_building_id' not in request.json
            or 'city_id' not in request.json):
            abort(400)
        new_building = request.get_json()
        if 'height' not in request.json:
            new_building['height'] = 0
        if 'year' not in request.json:
            new_building['year'] = 2000
        building_new = insert_building(new_building)
        return {'building': building_schema.dump(building_new)}, 201

class BuildingAPI(Resource):
    @auth.login_required
    def get(self, id):
        building = get_building(id)
        if building is None:
            abort(404)
        return {"building": building_schema.dump(building)}

    @auth.login_required
    def put(self, id):
        building = get_building(id)
        if building is None or not request.json:
            abort(404)
        if 'title' in request.json and type(request.json['title']) is not str:
            abort(400)
        if ('type_building_id' in request.json and
            type(request.json['type_building_id']) is not int):
            abort(400)
        if 'city_id' in request.json and type(request.json['city_id']) is not int:
            abort(400)
        if 'year' in request.json and type(request.json['year']) is not int:
            abort(400)
        if 'height' in request.json and type(request.json['height']) is not int:
            abort(400)
        building_update = update_building(id, request.get_json())
        return {'building': building_schema.dump(building_update)}

    @auth.login_required
    def delete(self, id):
        if delete_building(id):
            return {'result': True}
        abort(404)
