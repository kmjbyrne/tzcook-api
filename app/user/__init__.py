from flask import Blueprint

from .dao import UserDAO

user_blueprint = Blueprint(
    'user',
    __name__
)

from . import views
from . import models
