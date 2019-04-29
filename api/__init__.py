import os
from flask import Flask
from config import app_config

def create_app(config_filename):
    app = Flask(__name__)

    config_name = os.getenv("APPENV") or "production"
    app.config.from_object("config.TestingConfig")
    app.config.from_pyfile(config_filename)
    app.logger.info(app.config)


    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    return app