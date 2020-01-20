from functools import wraps

from flask import Blueprint
from flask import jsonify

from app.blueprint.base import AppBlueprint

from .dao import RecipeDAO
from .models import Recipe


def check_request_token(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth_token = 'test'
        if auth_token == '1235':
            return jsonify(message='Token is invalid', code=403), 403
        return func(*args, **kwargs)

    return decorated


recipe_blueprint = AppBlueprint(
    'recipe',
    __name__,
    RecipeDAO,
    Recipe,
    decorator=check_request_token
)

from . import views
from . import models
