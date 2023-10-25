from flask import Flask, jsonify
from flask_smorest import Api
from flask_session import Session
from flask_cors import CORS
from flask_migrate import Migrate
from db import db

import models


# from resources.accueil import blp as AccueilBlueprint

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)
    CORS(app)

    app.config["API_TITLE"] = "Projet4-HacktoberFest"
    app.config["API_VERSION"] = "v1.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/projethacktober'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/projethacktober'

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)

    with app.app_context():
        db.create_all()

    # api.register_blueprint(AccueilBlueprint)

    return app
