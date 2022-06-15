import os

from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_restful import Api
from flask_jwt_extended import JWTManager

from configs import get_config
from apps.routers import initial_routes
from helpers.exception import custom_json_exception, CustomJsonException
from helpers.encoder import encoder_response


def create_app():
    flask_app = Flask(__name__)
    CORS(flask_app, resources={r"/api/*": {"origins": "*"}})
    flask_app.config.update(get_config(os.getenv('FLASK_CONFIG_MODULE', 'local')))

    flask_app.register_error_handler(CustomJsonException, custom_json_exception)

    db = MongoEngine()
    db.init_app(flask_app)

    jwt = JWTManager()
    jwt.init_app(flask_app)

    flask_api = Api(flask_app)
    flask_api.representations.update({
        'application/json': encoder_response
    })
    initial_routes(flask_api)

    return flask_app


app = create_app()
host = os.getenv("FLASK_HOST", "0.0.0.0")
port = os.getenv("FLASK_PORT", 5000)

if __name__ == "__main__":
    app.run(host=host, port=port)
