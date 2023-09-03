import os

from flask import Flask
from flask_restful import Api
from .auth import *

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

    # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'
    # from .auth.index import index_bp
    # from .auth.auth import auth_bp
    from .auth.api import TodoSimple
    # app.register_blueprint(index_bp,  url_prefix='/')
    # app.register_blueprint(auth_bp,  url_prefix='/auth')
    api.add_resource(TodoSimple, '/<string:todo_id>')
    

    return app