from flask import jsonify, request

from . import model_bp
from app.utils.model_utils import extract_fault_event


@model_bp.route('/extractFault')
def extract_fault():
    sentence = request.args.get('sentence')
    res = extract_fault_event(sentence=sentence)
    res['sentence'] = sentence

    return jsonify(res)
