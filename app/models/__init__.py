from flask import Flask
from flask_migrate import Migrate
from config import config
from app.dbs import db

app = Flask(__name__)
app.config.from_object(config)
migrate = Migrate(app, db)
