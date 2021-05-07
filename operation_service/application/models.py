from . import db
from datetime import datetime


class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # hospital primary key reference
    hospital = db.Column(db.Integer, nullable=False)
    # surgery primary key reference
    surgery = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime)
    surgeon = db.Column(db.String(255))

    def to_json(self):
        return {
            'id': self.id,
            'hospital': self.hospital,
            'surgery': self.surgery,
            'price': self.price,
            'date': self.date,
            'surgeon': self.surgeon
        }
