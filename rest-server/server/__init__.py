from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin



server = Flask(__name__)
server.config.from_object(Config)
db = SQLAlchemy(server)
migrate = Migrate(server, db)
CORS(server)

from server import routes, models
