from datetime import datetime

from flask_electron.db.flaskalchemy.database import db
from flask_electron.db.flaskalchemy.database import DeclarativeBase


class Ingredient(DeclarativeBase):
    name = db.Column(db.String(120), nullable=False)
    calories = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
