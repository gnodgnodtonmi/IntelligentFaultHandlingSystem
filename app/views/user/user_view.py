from flask import request, jsonify

from . import user_bp
from app.models.model import User


@user_bp.route('/getCarTypeId', methods=['GET'])
def get_car_type_id():
    user_id = request.args.get('userId')
    users = User.query.filter_by(user_id=user_id).all()
    if len(users) != 0:
        user = users[0]
        return jsonify({'msg': 'success',
                        'data': {'user_id': user.user_id,
                                 'car_type': user.car_type}})
    else:
        return jsonify({'msg': 'failure',
                        'data': {}})
