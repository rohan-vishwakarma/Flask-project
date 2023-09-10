from flask_restful import Resource
from flask import request, Blueprint, jsonify


auth_bp = Blueprint('authentication' , __name__, url_prefix='/authentication')

@auth_bp.route('/')
def index():

    return "this is an authentication page"

