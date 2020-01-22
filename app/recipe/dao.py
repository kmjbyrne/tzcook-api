from flask_electron.dao.base import BaseDAO

from .models import Recipe


class RecipeDAO(BaseDAO):
    json = False

    def __init__(self, *args, **kwargs):
        super().__init__(Recipe, *args, **kwargs)
        self.model = Recipe
