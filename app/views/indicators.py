import datetime
from flask import Blueprint, render_template
from flask import request

from flask import Response

from app.logic.electro_logic import admin_pg_db, import_electro, select_electro, readcsv
from app.logic.electro_logic import add_node_electro, del_nodes_elctro


from app.views.base_except_view import base_view_except
from sqlalchemy.exc import SQLAlchemyError


indicators = Blueprint('indicators', __name__, template_folder='templates')


@indicators.route('/indicators')
@base_view_except
def indicators_show(name=None):
    # показывает таблицу electro из бд
    try:
        # from PGdatabase import select_electro
        t = select_electro()
        print("m")
        return render_template('indicators.html',  t=t.all())
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        return render_template('indicators.html',  t="")

    # versqlachemy()
    # testcreate()
    # testadd()
    # readcsv()



@indicators.route('/add_electro', methods=['GET', 'POST'])
@base_view_except
def add_electro():
    # добавляет показания счетчика из формы в бд еще не рботает
    # Добавление зпписи из формы в бд
    if request.method == "POST":
        number = request.form
        print(number['date'] +" " + number['number'])
        add_node_electro(month=number['date'], meter=number['number'])

    t = select_electro()
    print(t)
    return render_template('indicators.html',  t=t.all())


@indicators.route('/import_csv')
@base_view_except
def import_csv(name=None):
    # импортирует данные из csv
    print(datetime.datetime.today())
    import_electro()
    # versqlachemy()
    t = select_electro()
    return render_template('indicators.html',  t=t.all())


@indicators.route('/export_csv')
@base_view_except
def export_csv():
    # csv = '1,2,3\n4,5,6\n'
    csv1 = readcsv()
    j = []
    for i in csv1:
        x = ";".join(i)
        j.append(x)
    csv = "\n".join(j)
    # print(k)
    return Response(csv, mimetype="text/csv",
                    headers={"Content-disposition": "attachment; filename= myplot.csv"})


@indicators.route('/control')
@base_view_except
def del_nodes_electro():
    # Удаляет все записи в ELECTRO
    print(26)
    del_nodes_elctro()
    t = select_electro()
    return render_template('indicators.html',  t=t.all())



@indicators.route('/admin_pg')
@base_view_except
def admin_pg():
#     настроичная функция
    admin_pg_db()
