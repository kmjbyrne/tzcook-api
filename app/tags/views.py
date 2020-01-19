from flask import jsonify
from flask_electron.auth.decorators import check_request_token

from . import tag_blueprint
from .dao import TagDAO


@tag_blueprint.route('/test', methods=['GET'])
# @check_request_token
def get_all_ingredients():
    dao = TagDAO()
    ingredients = dao.query().all()
    return jsonify(data=ingredients.json(), schema=ingredients.schema)
