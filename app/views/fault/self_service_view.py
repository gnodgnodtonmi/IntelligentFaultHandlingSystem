from flask import jsonify, request

from . import fault_bp
from app.models.model import SystemFault, StructureFault, CellFault


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
        return jsonify({'msg': "missing 1 required argument \'faultId\'"})

    system_faults = SystemFault.query.filter_by(fault_id=system_fault_id).all()
    if len(system_faults) == 0:
        return jsonify({'msg': f'Can not found the SystemFault(faultId={system_fault_id})'})
    system_fault = system_faults[0]

    system_fault_name = system_fault.fault_name
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


@fault_bp.route('/getCellFaultById', methods=['GET'])
def get_cell_fault_by_id():
    struct_fault_id = request.args.get('faultId')
    if struct_fault_id is None:
        return jsonify({'msg': "missing 1 required argument \'faultId\'"})

    struct_faults = StructureFault.query.filter_by(fault_id=struct_fault_id).all()
    if len(struct_faults) == 0:
        return jsonify({'msg': f'Can not found the StructFault(faultId={struct_fault_id})'})
    struct_fault = struct_faults[0]

    struct_fault_name = struct_fault.fault_name
    cell_faults = CellFault.query.filter_by(parent_fault=struct_fault_id).all()
    res = {'msg': 'success',
           'struct_fault_name': struct_fault_name,
           'cell_fault_list': []}

    for cell_fault in cell_faults:
        cell_fault_id = cell_fault.fault_id
        cell_fault_name = cell_fault.fault_name
        data = {'fault_id': cell_fault_id,
                'fault_name': cell_fault_name}
        res['cell_fault_list'].append(data)

    return jsonify(res)
