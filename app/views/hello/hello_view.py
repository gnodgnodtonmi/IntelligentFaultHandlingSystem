from flask import jsonify

from . import hello_bp


@hello_bp.route('/helloWorld', methods=['GET'])
def hello_word():
    return jsonify({'msg': 'hello world'})
