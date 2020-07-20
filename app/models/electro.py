# from app import db
from app.extensions import db


class ELECTRO(db.Model):
    # структура данных Электро покаазаний
    __tablename__ = 'ELECTRO'

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String, nullable=True)
    typeMeter = db.Column(db.String, nullable=True)
    meter = db.Column(db.String, nullable=True)

    def __init__(self, month, typeMeter, meter):
        self.month = month
        self.typeMeter = typeMeter
        self.meter = meter

    def __repr__(self):
        return '%d, %s, %s, %s' % (self.id, self.month, self.typeMeter, self.meter)



