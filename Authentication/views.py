from flask_restful import Resource
from flask import  Blueprint, jsonify
from flask import request
from .models import User
from .models import db

auth_bp = Blueprint('authentication' , __name__, url_prefix='/authentication')

@auth_bp.route('/', methods = ['GET'])
def index():
    if User.query.filter_by(username="rohan").first():
        return f"username already exist"
    user = User(username="rohan", email="rohan@gmail.com", password="123456")
    execute = db.session.add(user)
    save = db.session.commit()
    db.session.close()
    if save:
        return jsonify({'message' : '"the user saved"'})
    
    return "this is an authentication page"


@auth_bp.route('/add', methods = ['POST', 'GET'])
def addUser():
    try:
        if request.method == "POST":
            username = request.form['username']
            email = request.form['username']
            password = request.form['password']
            getdata = None
            if username or email or password is not None:
                getdata = User.query.filter_by(username=username).first()
                if getdata is None:
                    user_obj = User(username=username, email=email, password=password)
                    execute = db.session.add(user_obj)
                    save = db.session.commit()
                    if save:
                        return f"{username} created successfully"
                else:
                    if getdata is not None:
                        return jsonify({'message' : f"{username} already exist"})
            return jsonify({'messgae': f"user {username} created successufully"})        
            
        else:
            if request.method == 'GET':
                return jsonify({"message" : "get method"})
    except Exception as e:
        return f"Exception occured {str(e)}"
