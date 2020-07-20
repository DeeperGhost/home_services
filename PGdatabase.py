import csv
# from models.electro import ELECTRO, db
# from sqlalchemy import create_engine, MetaData
#
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import Session

# from models.electro import ELECTRO2, db
# engine = create_engine('postgresql://' + POSTGRES_USER + ':' + POSTGRES_PW + '@localhost/' + POSTGRES_DB, echo=False)
# metadata = MetaData(bind=engine)
# session = Session(bind=engine)
# Base = declarative_base()
#


def admin_pg_db():
    # создает все таблицы
    print("Create_ALL")
    # Base.metadata.create_all(engine)
    #дропает все даблицы
    # Base.metadata.drop_all(engine)


def import_electro(month="00.00.0000", typeMeter= "По одноставочному тарифу", meter="000000"):
    # Функция для добавление записи в таблицу БД
    # на данный момент тестово импортит данные из csv

    with open('data/1.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        data = list(spamreader)

    index = 1
    while index < len(data):
        add_node_electro(month=data[index][0], typeMeter=data[index][1], meter=data[index][2])
        index += 1



def select_electro():
    # Выбор данных из БД
    from models.electro import db, ELECTRO
    return db.session.query(ELECTRO).order_by(ELECTRO.meter.desc())


def add_node_electro(month="", typeMeter="По одноставочному тарифу:", meter=""):
    #Добавить запись в таблицу electro
    from models.electro import db, ELECTRO
    node = ELECTRO(month=month, typeMeter=typeMeter, meter=meter)
    db.session.add(node)
    db.session.commit()


def readcsv():
    # читает csv файл с данными по электричетсву
    # возвращает список() тестируемый варифнт
    with open('data/1.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        data = list(spamreader)
        # spamreader.next()
    return data


def del_nodes_elctro():
    # удаляет записи из таблицы
    from models.electro import db, ELECTRO
    db.session.query(ELECTRO).delete()
    db.session.commit()


def drop_electro():
    from models.electro import ELECTRO
    # from main import db
    ELECTRO.__table__.drop()
    # session.


# def versqlachemy():
#     # выводит версию подключеной sqlAlchemy
#     print("Версия SQLAlchemy:", sqlalchemy.__version__)

