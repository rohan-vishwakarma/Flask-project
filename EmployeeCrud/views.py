from flask_restful import Resource
from flask import request, Blueprint, jsonify


employee_bp = Blueprint('employee' , __name__, url_prefix='/')

@employee_bp.route('/')

def index():
    return "this is a rest api"

data = {}

print(data)
@employee_bp.route('/Employee', methods = ['GET'])
def employee_list():
    if not bool(data):
        return {"message" : "list is empty"}
    return jsonify(data)



@employee_bp.route('/Employee/GET/<int:emp_id>', methods =['GET'])
def get_employee(emp_id):
    employee = data.get(emp_id)
    print(employee)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"message" : "employeee data not found..."})

@employee_bp.route('/Employee/POST/<string:name>', methods =['POST', 'GET'])
def add_employee(name):

    for entry in data.values():
        if entry['name'] == name:
            return {"message" : f"{name} already exist" }
    
    if bool(data) == True:
        max_is = max(data)
        id = int(max_is+1)
        data[id] = {}
        data[id]['name'] = name
        return jsonify(data)
    else:
        id = 1
        data[id] = {}
        data[id]['name'] = name
        return jsonify(data)

    return jsonify(data)


# @employee_bp.route('/Employee/<string:id>')
# def delete_employee(id):


    


    

