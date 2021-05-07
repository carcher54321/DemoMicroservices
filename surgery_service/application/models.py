from . import db
from datetime import datetime


class Surgery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(255), unique=True, nullable=False)
    severity = db.Column(db.Integer)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'severity': self.severity
        }
