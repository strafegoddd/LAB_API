from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
app.json.ensure_ascii = False

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'student':
        return 'dvfu'
    return None

@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'}), 401

class HelloWorld(Resource):
    def get(self):
        return {'app': 'Самые высокие здания и сооружения'}

api.add_resource(HelloWorld, '/')

from structures.resources import BuildingListAPI, BuildingAPI
api.add_resource(BuildingListAPI, '/structures/api/v1/buildings')
api.add_resource(BuildingAPI, '/structures/api/v1/buildings/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)

import structures.views