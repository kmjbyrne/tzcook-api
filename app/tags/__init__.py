from flask import Blueprint
from app.blueprint.base import AppBlueprint

from .dao import TagDAO
from .models import Tag

tag_blueprint = AppBlueprint(
    'tag',
    __name__,
    TagDAO,
    Tag
)

from . import views
from . import models
