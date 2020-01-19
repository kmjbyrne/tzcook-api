from flask import Blueprint
from app.blueprint.base import AppBlueprint

from .dao import CategoryDAO
from .models import Category

category_blueprint = AppBlueprint(
    'category',
    __name__,
    CategoryDAO,
    Category
)

from . import views
from . import models
