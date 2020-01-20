from flask import Blueprint
from app.blueprint.base import AppBlueprint

from .dao import UserDAO

user_blueprint = AppBlueprint(
    'user',
    __name__,
    UserDAO,
    UserDAO.model
)

from . import views
from . import models
