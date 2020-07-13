from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import datetime
indicators = Blueprint('indicators', __name__,
                        template_folder='templates')

from PGdatabase import initPGdb, addElectro, selectElectro


@indicators.route('/indicators')
def indicatorsShow(name=None):

    print("a")
    # versqlachemy()
    # testcreate()
    # testadd()
    # readcsv()

    try:
        return render_template('indicators.html', name=name, t="")
    except TemplateNotFound:
        abort(404)


@indicators.route('/douwnloadCSV')
def douwnloadCSV(name=None):
    print(datetime.datetime.today())
    # initPGdb()
    # versqlachemy()

    # addElectro()
    t = selectElectro()
    print(t[0])
    i=0
    print(t.all())
    return render_template('indicators.html', name=name, t=t.all())


# @indicators.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()
