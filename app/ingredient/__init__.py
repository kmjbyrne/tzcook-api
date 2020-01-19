from app.blueprint.base import AppBlueprint

from .dao import IngredientDAO
from .models import Ingredient

ingredient_blueprint = AppBlueprint(
    'ingredient',
    __name__,
    IngredientDAO,
    Ingredient
)

from . import views
from . import models
