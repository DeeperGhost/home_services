from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import POSTGRES_URL, POSTGRES_USER, POSTGRES_PW, POSTGRES_DB
from config import HOST, PORT, DEBUG

from views.indicators import indicators
from views.upload import upload
from views.basic_view import basic_view


app = Flask(__name__)
app.register_blueprint(indicators)
app.register_blueprint(upload)
app.register_blueprint(basic_view)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + \
                                        POSTGRES_USER + ':' + POSTGRES_PW + '@localhost/' + POSTGRES_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     session.remove()
#

if __name__ == '__main__':
    app.run(host=HOST,port= PORT, debug=DEBUG)
