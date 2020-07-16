from flask import Blueprint, render_template

import datetime

from flask import Response

from PGdatabase import initPGdb, import_electro, select_electro, readcsv
from views.base_except_view import base_view_except


indicators = Blueprint('indicators', __name__, template_folder='templates')

@indicators.route('/indicators')
@base_view_except
def indicators_show(name=None):
    t = select_electro()
    print("m")
    # versqlachemy()
    # testcreate()
    # testadd()
    # readcsv()
    return render_template('indicators.html', name=name, t=t.all())


@indicators.route('/downloadCSV')
@base_view_except
def download_csv(name=None):
    print(datetime.datetime.today())
    # initPGdb()
    # versqlachemy()

    # addElectro()

    return render_template('indicators.html', name=name, t="")


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

# @indicators.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()
