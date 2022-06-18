from flask import jsonify

from . import fault_bp


@fault_bp.route('/getAllSystemFaults')
def get_all_system_faults():
    pass
