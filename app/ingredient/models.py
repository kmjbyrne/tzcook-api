from datetime import datetime

from flask_electron.db.flaskalchemy.database import db
from flask_electron.db.flaskalchemy.database import DeclarativeBase


class Ingredient(DeclarativeBase):
    name = db.Column(db.String(120), nullable=False)

    measure_id = db.Column(db.Integer, db.ForeignKey('measure.id'), nullable=True)
    measure = db.relationship('Measure', backref='ingredient', cascade='all', uselist=False)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=True)
    recipe = db.relationship('Recipe', back_populates='ingredient', cascade='all', uselist=False)

    def __repr__(self):
        return self.name


class Measure(DeclarativeBase):
    unit = db.Column(db.String(120), nullable=False)
    short = db.Column(db.String(120), nullable=False)

    # measure = db.relationship('Ingredient', backref='measure', cascade='all', uselist=False)

    def __repr__(self):
        return self.unit
