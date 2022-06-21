import os

from flask import jsonify, request

from . import model_bp
from app.utils.model_utils import extract_fault_event, text_semantic_matching
from app.models.model import CellFault, Solution, Step, Pictures, SystemFault, StructureFault
from app.views.solution.solution_view import picture_prefix


@model_bp.route('/extractFault', methods=['GET'])
def extract_fault():
    sentence = request.args.get('sentence')
    res = extract_fault_event(sentence=sentence)
    res['sentence'] = sentence

    return jsonify(res)


@model_bp.route('/autoLocateFault', methods=['GET'])
def auto_locate_fault():
    sentence = request.args.get('sentence')
    event_res = extract_fault_event(sentence=sentence)

    res = dict()

    if len(event_res.items()) == 0 or event_res['fault_location'] is None:
        cell_faults = CellFault.query.all()
        cell_fault_name_list = [cf.fault_name for cf in cell_faults]

        res_match = text_semantic_matching(sentence, cell_fault_name_list)
        match_index = res_match['match_index']
        cell_fault = cell_faults[match_index]

    else:
        fault_location = event_res['fault_location']
        system_faults = SystemFault.query.all()
        system_fault_name_list = [sf.fault_name for sf in system_faults]

        sys_res_match = text_semantic_matching(fault_location, system_fault_name_list)
        sys_match_index = sys_res_match['match_index']
        system_fault = system_faults[sys_match_index]
        system_fault_id = system_fault.fault_id

        struct_faults = StructureFault.query.filter_by(parent_fault=system_fault_id).all()
        cell_fault_list = []
        for struct_fault in struct_faults:
            struct_fault_id = struct_fault.fault_id
            cell_faults = CellFault.query.filter_by(parent_fault=struct_fault_id).all()
            cell_fault_list.extend(cell_faults)

        cell_fault_name_list = [cf.fault_name for cf in cell_fault_list]
        res_match = text_semantic_matching(sentence, cell_fault_name_list)
        match_index = res_match['match_index']
        cell_fault = cell_fault_list[match_index]

    cell_fault_id = cell_fault.fault_id
    cell_fault_name = cell_fault.fault_name
    cell_fault_type = cell_fault.fault_type
    fault_data = {'fault_id': cell_fault_id,
                  'fault_name': cell_fault_name,
                  'fault_type': cell_fault_type}

    solution_id = cell_fault.solution
    solutions = Solution.query.filter_by(solution_id=solution_id).all()
    solution = solutions[0]

    solution_title = solution.title
    solution_steps = solution.step.split('-')

    step_list = []
    for step_id in solution_steps:
        single_step = {}
        steps = Step.query.filter_by(step_id=step_id).all()
        assert len(steps) != 0
        step = steps[0]
        step_content = step.content
        single_step['content'] = step_content

        picture_id = step.picture_id
        picture_path = None
        if picture_id is not None:
            picture = Pictures.query.filter_by(picture_id=picture_id).all()[0]
            picture_path = os.path.join(picture_prefix, picture.picture_path[1:])
        single_step['picture_path'] = picture_path

        step_list.append(single_step)

    res['fault'] = fault_data
    solution_data = {'solution_id': solution_id,
                     'title': solution_title,
                     'step_list': step_list}
    res['solution'] = solution_data

    return jsonify(res)
