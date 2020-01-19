from flask import Blueprint
from app.blueprint.base import AppBlueprint

from .dao import RecipeDAO
from .models import Recipe

recipe_blueprint = AppBlueprint(
    'recipe',
    __name__,
    RecipeDAO,
    Recipe
)

from . import views
from . import models
