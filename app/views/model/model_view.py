from flask import jsonify, request

from . import model_bp, ie


@model_bp.route('/extractFaultEvent')
def extract_fault_event():
    sentence = request.args.get('sentence')
    res = ie([sentence])
    res = res[0]
    res['sentence'] = sentence

    return jsonify(res)
