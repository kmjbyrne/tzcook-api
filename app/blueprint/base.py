from flask import jsonify
from flask import Blueprint
from flask import request
from flask_electron.dao.base import BaseDAO
from flask_electron.auth.decorators import check_request_token


class AppBlueprint(Blueprint):

    def __init__(self, name, module, dao=None, model=None):
        if dao is None:
            self.dao = BaseDAO
            self.dao.model = model
        self.dao = dao
        self.model = model
        super().__init__(name, module)
        self.register_generic_routes()

    def get_handler_name(self):
        return '{}_{}'.format(self.name, 'get')

    # @check_request_token
    def default_get_request(self):
        data = self.dao().query().all()
        return jsonify(data=data.json() or dict(), schema=data.schema), 200

    def default_get_one_request(self, resource):
        data = self.dao().get_one(resource)
        if data.data is None:
            return jsonify(data=dict(), schema=data.schema), 404
        return jsonify(data=data.json() or dict(), schema=data.schema), 200

    def default_post_request(self, *args, **kwargs):
        payload = request.json
        instance = self.dao().create(payload).prepare(json=True)
        return jsonify(instance), 200

    def register_generic_routes(self):
        self.add_url_rule('', 'get', self.default_get_request, methods=['GET'])
        self.add_url_rule('/<resource>', 'one', self.default_get_one_request, methods=['GET'])
        self.add_url_rule('', 'create', self.default_post_request, methods=['POST'])
        self.add_url_rule('/', 'update', self.default_get_request, methods=['PUT'])
        self.add_url_rule('/', 'delete', self.default_get_request, methods=['DELETE'])
        self.add_url_rule('/', 'patch', self.default_get_request, methods=['PATCH'])
