from flask import Flask
from flask_migrate import Migrate

from config import config
from app.dbs import db
from app.views.hello import hello_bp
from app.views.user import user_bp
from app.views.fault import fault_bp
from app.views.model import model_bp
from app.views.solution import solution_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(hello_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(fault_bp)
    app.register_blueprint(model_bp)
    app.register_blueprint(solution_bp)

    db.init_app(app)
    migrate = Migrate(app, db)

    return app, migrate
