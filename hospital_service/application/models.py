from . import db
from datetime import datetime


class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    zip = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(255), unique=True, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'zip': self.zip,
            'code': self.code
        }
