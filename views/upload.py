import flask
from flask import Blueprint, render_template, jsonify, abort

from jinja2 import TemplateNotFound

from config import pathWork


upload = Blueprint('upload', __name__,
                       template_folder='templates')


@upload.route('/upload', methods=['GET', 'POST'])
def uploadFiles():
    # Загрузка файлов на сервер
    try:
        if flask.request.method == "POST":

            files = flask.request.files.getlist("files")

            # Не пустой ли список файлов
            if files[0].filename == '':
                return render_template('upload.html')

            count = 0
            for file in files:

                file.save(pathWork+file.filename)
                count += 1
            print(count)
            return jsonify(htmtext='upload.html', count=count, cou= 666)
        else:
            return render_template('upload.html', count=0)
    except TemplateNotFound:
        abort(404)

