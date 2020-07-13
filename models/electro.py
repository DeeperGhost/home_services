#
from sqlalchemy import Table, Column, Integer, String,  ForeignKey
from PGdatabase import Base

# структура данных Электро покаазаний
class ELECTRO(Base):
    __tablename__ = 'ELECTRO'

    id = Column(Integer, primary_key=True)
    month = Column(String, nullable=True)
    typeMeter = Column(String, nullable=True)
    meter = Column(String, nullable=True)

    def __init__(self, month, typeMeter, meter):
        self.month = month
        self.typeMeter = typeMeter
        self.meter = meter

    def __repr__(self):
        return '%d, %s, %s, %s' % (self.id, self.month, self.typeMeter, self.meter)
        # return "<ELECTRO('%d, %s, %s, %s')>" % (self.id, self.month, self.typeMeter, self.meter)