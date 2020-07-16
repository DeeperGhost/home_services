import sqlalchemy
import csv

from sqlalchemy import create_engine
from sqlalchemy import MetaData

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from config import POSTGRES_URL, POSTGRES_USER, POSTGRES_PW, POSTGRES_DB


engine = create_engine('postgresql://' + POSTGRES_USER + ':' + POSTGRES_PW + '@localhost/' + POSTGRES_DB)

metadata = MetaData(bind=engine)
session = Session(bind=engine)
Base = declarative_base()


def initPGdb():
    # создает все таблицы
    Base.metadata.create_all(engine)


def import_electro(month="00.00.0000", typeMeter= "По одноставочному тарифу", meter="000000"):
    # Функция для добавление записи в таблицу БД
    # на данный момент тестово импортит данные из csv
    from models.electro import ELECTRO

    data = readcsv()
    index = 1
    while index < len(data):
        print(data[index])
        node = ELECTRO(month=data[index][0], typeMeter=data[index][1], meter=data[index][2])
        session.add(node)
        session.commit()

        print(index)
        index += 1


def select_electro():
    # Выбор данных из БД
    from models.electro import ELECTRO

    return session.query(ELECTRO)
    # for electro in session.query(ELECTRO):#.filter_by(month='24.06.2020'):
    #     print(electro.month)
    #     print(electro)


def versqlachemy():
    # выводит версию подключеной sqlAlchemy
    print("Версия SQLAlchemy:", sqlalchemy.__version__)  # посмотреть версию SQLALchemy


def readcsv():
    # читает csv файл с данными по электричетсву
    # возвращает список() тестируемый варифнт
    with open('data/1.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        data = list(spamreader)
        # spamreader.next()
        return data
