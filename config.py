from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///structure.db'

db.init_app(app)