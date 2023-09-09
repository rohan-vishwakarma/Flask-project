import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .models import db


app = None
api = None
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    # Create the database tables
    with app.app_context():
        db.create_all()
    



    

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
    
    app.register_blueprint(employee_bp)
    
    

    return app