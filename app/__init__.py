from flask import Flask

from app.extensions import db, migrate
from config import POSTGRES_USER, POSTGRES_PW, POSTGRES_DB

from app.views.indicators import indicators
from app.views.upload import upload
from app.views.basic_view import basic_view


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + \
                                            POSTGRES_USER + ':' + POSTGRES_PW + '@localhost/' + POSTGRES_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    register_extensions(app)
    register_blueprints(app)
    # app.run(host=host, port=port, debug=debug)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(indicators)
    app.register_blueprint(upload)
    app.register_blueprint(basic_view)
