import flask

from config import HOST, PORT, DEBUG
from config import indicatorsPath, pathWork



from flask import Flask, json, request
from flask import render_template





from views.indicators import indicators
from views.upload import upload

app = Flask(__name__)
app.register_blueprint(indicators)
app.register_blueprint(upload)


@app.route('/')
def index():
    f = open(indicatorsPath, 'r')
    indicator = f.readline()
    f.close()

    hum = indicator[0:2]
    temp = indicator[3:5]

    return render_template('index.html', hum= hum, temp= temp)










@app.route('/test')
def test(name=None):
    return render_template('test.html', name=name)


@app.route('/get_len', methods=['GET', 'POST'])
def get_len():
    name = request.form['name'];
    return json.dumps({'len': len(name)})






if __name__ == '__main__':
    app.run(host=HOST,port= PORT, debug=DEBUG)