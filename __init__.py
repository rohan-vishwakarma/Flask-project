import os

from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_mysqldb import MySQL
from jinja2 import ChoiceLoader, FileSystemLoader

from .Authentication.models import db


migrate = Migrate()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    templates = ['Frontend/templates', 'layout/templates']
    template_loader = ChoiceLoader([FileSystemLoader(template) for template in templates])
    app.jinja_loader = template_loader

    api = Api(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rohan84.20@localhost/flaskdb'

    app.config['SQLALCHEMY_BINDS'] = {
    'flaskdb': 'mysql://root:Rohan84.20@localhost/flaskdb',
    }


    mysql = MySQL(app)

    db.init_app(app)
    migrate.init_app(app, db)
    # Create the database tables


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .EmployeeCrud.views import employee_bp
    from .Authentication.views import auth_bp
    from .Authentication.frontend import front_bp
    
    app.register_blueprint(employee_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(front_bp)

    return app