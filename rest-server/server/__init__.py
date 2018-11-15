from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager


server = Flask(__name__)
server.config.from_object(Config)
  
db = SQLAlchemy(server)
migrate = Migrate(server, db)
CORS(server)

jwt = JWTManager(server)


from server import routes, models
