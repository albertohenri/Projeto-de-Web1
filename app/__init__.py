
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager




def create_app(config_name):
    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    return app

app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
migrate = Migrate(app, db)



manager = Manager(app)
manager.add_command('db', MigrateCommand)


lm = LoginManager()
lm.init_app(app)

from app.models import tables ,forms
from app.controllers import default


def create_app(config_name):
    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    return app








