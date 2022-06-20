import os

from flask import jsonify, request

from . import solution_bp
from app.models.model import CellFault, Solution, Step, Pictures

picture_prefix = 'localhost:5000'


@solution_bp.route('/getSolutionByFaultId')
def get_solution_by_fault_id():
    cell_fault_id = request.args.get('faultId')
    if cell_fault_id is None:
        return jsonify({'msg': "missing 1 required argument \'faultId\'"})

    cell_faults = CellFault.query.filter_by(fault_id=cell_fault_id).all()
    if len(cell_faults) == 0:
        return jsonify({'msg': f'Can not found the CellFault(faultId={cell_fault_id})'})
    cell_fault = cell_faults[0]

    cell_fault_name = cell_fault.fault_name
    solution_id = cell_fault.solution
    solutions = Solution.query.filter_by(solution_id=solution_id).all()
    if len(solutions) == 0:
        return jsonify({'msg': f'Can not found the CellFault(faultId={solution_id})'})
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

    res = {'fault_id': cell_fault_id,
           'fault_name': cell_fault_name}
    solution_data = {'solution_id': solution_id,
                     'title': solution_title,
                     'step_list': step_list}
    res['solution_data'] = solution_data

    return jsonify(res)
