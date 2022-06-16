from flask import Flask
from flask_migrate import Migrate

from config import config
from app.dbs import db
from app.views.hello import hello_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(hello_bp)

    db.init_app(app)
    migrate = Migrate(app, db)

    return app
