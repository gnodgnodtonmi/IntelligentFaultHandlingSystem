from flask import jsonify, request

from . import fault_bp
from app.models.model import SystemFault, StructureFault


@fault_bp.route('/getAllSystemFaults', methods=['GET'])
def get_all_system_faults():
    system_faults = SystemFault.query.all()
    res = {'system_fault_list': []}

    for sf in system_faults:
        fault_id = sf.fault_id
        fault_name = sf.fault_name
        data = {'fault_id': fault_id,
                'fault_name': fault_name}
        res['system_fault_list'].append(data)

    return jsonify(res)


@fault_bp.route('/getStructureFaultById', methods=['GET'])
def get_structure_fault_by_id():
    system_fault_id = request.args.get('faultId')
    if system_fault_id is None:
        return jsonify({'msg': "missing 1 required argument \'fault_id\'"})

    system_faults = SystemFault.query.filter_by(fault_id=system_fault_id).all()[0]
    system_fault_name = system_faults.fault_name
    struct_faults = StructureFault.query.filter_by(parent_fault=system_fault_id).all()
    res = {'msg': 'success',
           'system_fault_name': system_fault_name,
           'struct_fault_list': []}

    for struct_fault in struct_faults:
        struct_fault_id = struct_fault.fault_id
        struct_fault_name = struct_fault.fault_name
        data = {'fault_id': struct_fault_id,
                'fault_name': struct_fault_name}
        res['struct_fault_list'].append(data)

    return jsonify(res)
