"""
Base classes for use in the testing scripts
"""
from flask_testing import LiveServerTestCase
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


class BaseTestCase(LiveServerTestCase):
    """ Base Tests """

    def create_app(self):
        app = Flask(__name__)
        app.config.from_object(Config)
        db = SQLAlchemy(app)
        migrate = Migrate(app, db)
        login_manager = LoginManager(app)
        login_manager.login_view = 'login'
        return app
