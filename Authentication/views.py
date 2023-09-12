from flask_restful import Resource
from flask import  Blueprint, jsonify, render_template
from flask import request
from .models import User
from .models import db

from sqlalchemy.exc import SQLAlchemyError

from .forms import UserForm


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


@auth_bp.route('/add', methods = ['POST'])
def addUser():
    try:
        if request.method == "POST":
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            getdata = None
            if username is not None and email is not None and password is not None:
                getdata = User.query.filter_by(username=username).first()
                if bool(getdata) is False:
                    user_obj = User(username=username, email=email, password=password)
                    execute = db.session.add(user_obj)
                    save = db.session.commit()
                    if save:
                        return f"{username} created successfully"
                else:
                    if bool(getdata) is True:
                        return jsonify({'message' : f"{username} already exist"})
            else:
                validation = {}
                if username is None:
                    validation['username_error'] = f" username cannot be empty"
                
                if email is None:
                    validation['email_error'] = f" email cannot be empty"
                
                if password is None:
                    validation['password_error'] = f" password cannot be empty"

                return jsonify(validation), 400
            
            return None       

    except SQLAlchemyError as e:
        db.session.rollback()
        return f"Database Exception occurred: {str(e)}", 500 

    except Exception as e:
        return f"Exception occured {str(e)}"
