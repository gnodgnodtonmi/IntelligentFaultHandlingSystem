from flask import Blueprint

solution_bp = Blueprint("solution", __name__, url_prefix='/solution')

from . import solution_view
