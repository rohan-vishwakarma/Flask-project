from .. import api
from flask_restful import Resource
from flask import request

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        try:
            if todo_id in todos:
                return {"message":f"{todo_id} already exists"}
            todos[todo_id] = {}
            todos[todo_id]["data"] = request.form['data']
            todos[todo_id]["method"]="PUT"
            return {todo_id: todos[todo_id]}
        except Exception as e:
            print(e)
    
    def delete(self, todo_id):
        return {todo_id: todos.pop(todo_id)}

    def post(self, todo_id):
        try:
            if todo_id in todos:
                return {"message":f"{todo_id} already exists"}
            todos[todo_id] = {}
            todos[todo_id]["data"] = request.form['data']
            todos[todo_id]["method"]="POST"
            return {todo_id: todos[todo_id]}
        except Exception as e:
            print(e)
    
    def patch(self, todo_id):
        data = []
        for dt in todos:
            data.append({dt: todos[dt]})
        return data



