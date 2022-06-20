from flask import jsonify, request

from . import model_bp
from app.utils.model_utils import extract_fault_event, text_semantic_matching


@model_bp.route('/extractFault', methods=['GET'])
def extract_fault():
    sentence = request.args.get('sentence')
    res = extract_fault_event(sentence=sentence)
    res['sentence'] = sentence

    return jsonify(res)


@model_bp.route('/AutoLocateFault', methods=['GET'])
def AutoLocateFault():
    sentence = request.args.get('sentence')
