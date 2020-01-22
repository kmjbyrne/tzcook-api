from datetime import datetime

from flask_electron.db.flaskalchemy.database import db
from flask_electron.db.flaskalchemy.database import DeclarativeBase


class Recipe(DeclarativeBase):
    __tablename__ = 'recipe'
    name = db.Column(db.String(120), nullable=False)
    created = db.Column(db.Date, nullable=True)
    time = db.Column(db.Integer, nullable=True)
    portions = db.Column(db.SmallInteger)
    image = db.Column(db.String(512), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship('User', backref='recipe', cascade='all', uselist=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    category = db.relationship('Category', backref='recipe', cascade='all', uselist=False)

    ingredient = db.relationship('Ingredient', back_populates='recipe')

    def __repr__(self):
        return self.name


class Step(DeclarativeBase):
    __tablename__ = 'steps'
    step = db.Column(db.Text, nullable=False)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=True)
    recipe = db.relationship('Recipe', backref='steps', cascade='all', uselist=False)

    def __repr__(self):
        return self.step
