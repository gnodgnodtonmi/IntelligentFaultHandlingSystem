from flask import jsonify

from . import fault_bp
from app.models.model import SystemFault


@fault_bp.route('/getAllSystemFaults', methods=['GET'])
def get_all_system_faults():
    system_faults = SystemFault.query.all()
    res = {'data': []}

    for sf in system_faults:
        fault_id = sf.fault_id
        fault_name = sf.fault_name
        data = {'fault_id': fault_id,
                'fault_name': fault_name}
        res['data'].append(data)

    return jsonify(res)
