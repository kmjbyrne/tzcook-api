from flask_electron.dao.base import BaseDAO

from .models import Ingredient


class IngredientDAO(BaseDAO):
    json = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = Ingredient
