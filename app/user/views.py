from flask import jsonify
from flask_electron.auth.decorators import check_request_token

from . import user_blueprint
from .dao import UserDAO


@user_blueprint.route('/', methods=['GET'])
# @check_request_token
def get_all_users():
    dao = UserDAO()
    users = dao.query().all()
    return jsonify(data=users.json(), schema=users.schema)
