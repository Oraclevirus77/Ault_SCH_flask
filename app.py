from flask import Flask, request, Response
from typing import List, Dict
from utils import parse_todo_request, save_todo
import json


# create a new todo
# edit a new todo
# delete a new todo
# get all todos
# get a single todo


app = Flask(__name__)


todos_list: List[Dict] = []
total_todos = 0


@app.route('/')
def hello_world():  # put application code here
    return 'Hello World'


@app.route('/todos', methods=['GET', 'POST'])
def new_todos():
    global total_todos
    global todos_list
    if request.method == 'GET':
        return Response( json.dumps(todos_list), status=200, mimetype='application/json' )


    request_data = request.get_json()
    todo = parse_todo_request(request_data)
    if None in todo.values():
        return Response(
            'Invalid request',
            status=400,
            mimetype='application/json'
        )
    save_todo(todo , todos_list)
    total_todos += 1 
    return Response(
        json.dumps(todo), 
        status=201,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(debug=True)
