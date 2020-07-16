import flask
from flask import Blueprint, render_template, jsonify

from config import pathWork
from views.base_except_view import base_view_except


upload = Blueprint('upload', __name__, template_folder='templates')


@upload.route('/upload', methods=['GET', 'POST'])
@base_view_except
def upload_files():
    # Загрузка файлов на сервер
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


