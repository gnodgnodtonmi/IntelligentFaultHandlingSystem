from flask import Blueprint

hello_bp = Blueprint("hello", __name__, url_prefix='/hello')

from . import hello_view
