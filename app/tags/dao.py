from flask_electron.dao.base import BaseDAO

from .models import Tag


class TagDAO(BaseDAO):
    json = False

    def __init__(self, *args, **kwargs):
        super().__init__(Tag, *args, **kwargs)
        self.model = Tag
