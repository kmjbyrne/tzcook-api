from datetime import datetime

from flask_electron.db.flaskalchemy.database import db
from flask_electron.db.flaskalchemy.database import DeclarativeBase


class Recipe(DeclarativeBase):
    __tablename__ = 'recipe'
    name = db.Column(db.String(120), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    category = db.relationship('Category', backref='recipe', cascade='all', uselist=False)
