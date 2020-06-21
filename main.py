from flask import Flask, url_for, flash
import flask
from flask import request
from flask import render_template
from werkzeug import Request


app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if flask.request.method == "POST" :

        files = flask.request.files.getlist("files")
        # Не пустой ли список файлов
        if files[0].filename == '':
            return render_template('upload.html')

        for file in files:
            file.save('C:/Users/007/PycharmProjects/FlaskServTest/data/'+file.filename)
    return render_template('upload.html')


@app.route('/upload2', methods=['GET', 'POST'])
def upload_file2():

    return render_template('upload2.html')




if __name__ == '__main__':
    app.run(host='192.168.0.102',port= 5000, debug=True)