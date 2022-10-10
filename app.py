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


@app.route('/todos', methods=['POST'])
def new_todos():
    global total_todos
    global todos_list
    request_data = request.get_json()
    todo = parse_todo_request(request_data)
    if None in todo.values():
        response = Response = Response(
            "Invalid request",
            status=400,
            mimetype='application/json'
        )
        return response
    save_todo(todo, todos_list)
    total_todos += 1
    response: Response = Response(
        json.dumps(todo),
        satus=201,
        mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run
