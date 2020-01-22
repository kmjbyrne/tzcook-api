from datetime import datetime

from flask_electron.db.flaskalchemy.database import db
from flask_electron.db.models.user.user import BaseUser
from sqlalchemy.ext.hybrid import hybrid_property


class User(BaseUser):
    __tablename__ = 'user'
    extend_existing = True
    created = db.Column(db.DateTime(), default=datetime.now())
    last_logged_in = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return self.fullname
    
    @hybrid_property
    def fullname(self):
        return '{} {}'.format(self.forename, self.surname)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.created = datetime.now()

    def name(self):
        return '{} {}'.format(self.forename, self.surname)
