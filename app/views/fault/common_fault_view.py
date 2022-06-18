from flask import jsonify

from . import fault_bp
from app.models.model import CommonFault, CellFault


@fault_bp.route('/getCommonFault', methods=['GET'])
def get_common_fault():
    common_faults = CommonFault.query.all()
    res = {'data': []}

    for comm_ft in common_faults:
        common_fault_id = comm_ft.common_fault_id
        cell_fault_id = comm_ft.cell_fault

        cf = CellFault.query.filter_by(fault_id=cell_fault_id).first()
        fault_name = cf.fault_name

        data = {'common_fault_id': common_fault_id,
                'cell_fault_id': cell_fault_id,
                'fault_name': fault_name}
        res['data'].append(data)

    return jsonify(res)
