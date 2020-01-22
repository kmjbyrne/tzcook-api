from flask_electron.dao.base import BaseDAO

from .models import Category


class CategoryDAO(BaseDAO):
    json = False

    def __init__(self, *args, **kwargs):
        super().__init__(Category, *args, **kwargs)
        self.model = Category
