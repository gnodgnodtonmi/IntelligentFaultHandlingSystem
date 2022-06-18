from flask import Blueprint

fault_bp = Blueprint("fault", __name__, url_prefix='/fault')

from . import common_fault_view
