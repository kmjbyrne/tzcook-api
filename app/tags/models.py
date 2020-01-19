from datetime import datetime

from flask_electron.db.flaskalchemy.database import db
from flask_electron.db.flaskalchemy.database import DeclarativeBase


class Tag(DeclarativeBase):
    name = db.Column(db.String(120), nullable=False)
    # recipes = db.relationship('Votes', backref='recipe', cascade='all, delete-orphan', lazy='dynamic')
