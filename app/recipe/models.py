from datetime import datetime

from flask_electron.db.flaskalchemy.database import db
from flask_electron.db.flaskalchemy.database import DeclarativeBase


class Recipe(DeclarativeBase):
    __tablename__ = 'recipe'
    name = db.Column(db.String(120), nullable=False)
    method = db.Column(db.Text, nullable=True)
    created = db.Column(db.Date, nullable=True)
    time = db.Column(db.Integer, nullable=True)
    portions = db.Column(db.SmallInteger)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship('User', backref='recipe', cascade='all', uselist=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    category = db.relationship('Category', backref='recipe', cascade='all', uselist=False)
