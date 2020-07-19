import sqlalchemy
import csv

from sqlalchemy import create_engine, MetaData

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from config import POSTGRES_URL, POSTGRES_USER, POSTGRES_PW, POSTGRES_DB


engine = create_engine('postgresql://' + POSTGRES_USER + ':' + POSTGRES_PW + '@localhost/' + POSTGRES_DB)
metadata = MetaData(bind=engine)
session = Session(bind=engine)
Base = declarative_base()



def admin_pg_db():
    # создает все таблицы
    Base.metadata.create_all(engine)
    #дропает все даблицы
    # Base.metadata.drop_all(engine)


def import_electro(month="00.00.0000", typeMeter= "По одноставочному тарифу", meter="000000"):
    # Функция для добавление записи в таблицу БД
    # на данный момент тестово импортит данные из csv
    from models.electro import ELECTRO

    with open('data/1.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        data = list(spamreader)

    index = 1
    while index < len(data):
        add_node_electro(month=data[index][0], typeMeter=data[index][1], meter=data[index][2])
        # node = ELECTRO(month=data[index][0], typeMeter=data[index][1], meter=data[index][2])
        # session.add(node)
        # session.commit()
        index += 1



def select_electro():
    # Выбор данных из БД
    from models.electro import ELECTRO

    return session.query(ELECTRO).order_by(ELECTRO.meter.desc())
    # for electro in session.query(ELECTRO):#.filter_by(month='24.06.2020'):
    #     print(electro.month)
    #     print(electro)


def add_node_electro(month="", typeMeter="По одноставочному тарифу:", meter=""):
    #Добавить запись в таблицу electro
    from models.electro import ELECTRO
    node = ELECTRO(month=month, typeMeter=typeMeter, meter=meter)
    session.add(node)
    session.commit()


def versqlachemy():
    # выводит версию подключеной sqlAlchemy
    print("Версия SQLAlchemy:", sqlalchemy.__version__)


def readcsv():
    # читает csv файл с данными по электричетсву
    # возвращает список() тестируемый варифнт
    with open('data/1.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        data = list(spamreader)
        # spamreader.next()
    return data


def del_nodes_elctro():
    from models.electro import ELECTRO
    session.query(ELECTRO).delete()
    session.commit()

def drop_electro():
    from models.electro import ELECTRO
    ELECTRO.__table__.drop(engine)
    # session.
