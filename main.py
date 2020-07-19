import flask
from flask import Flask, json, request,render_template

from config import HOST, PORT, DEBUG
from config import indicatorsPath, pathWork

from views.base_except_view import base_view_except
from views.indicators import indicators
from views.upload import upload

from PGdatabase import session


app = Flask(__name__)
app.register_blueprint(indicators)
app.register_blueprint(upload)



@app.route('/')
@base_view_except
def index():
    f = open(indicatorsPath, 'r')
    indicator = f.readline()
    f.close()

    hum = indicator[0:2]
    temp = indicator[3:5]
    return render_template('index.html', hum= hum, temp= temp)


@app.route('/test')
@base_view_except
def test(name=None):
    return render_template('test.html', name=name)


@app.route('/get_len', methods=['GET', 'POST'])
@base_view_except
def get_len():
    name = request.form['name'];
    return json.dumps({'len': len(name)})


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     session.remove()
#

if __name__ == '__main__':
    app.run(host=HOST,port= PORT, debug=DEBUG)