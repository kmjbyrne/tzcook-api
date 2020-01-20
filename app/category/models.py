from datetime import datetime

from flask_electron.db.flaskalchemy.database import db
from flask_electron.db.flaskalchemy.database import DeclarativeBase


class Category(DeclarativeBase):
    name = db.Column(db.String(120), nullable=False)
