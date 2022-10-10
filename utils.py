from typing import List, Dict, NoReturn
from datetime import datetime
import uuid


def parse_todo_request(request: Dict) -> Dict:
    """
    parse the request from a client and return the date in a dict
    :param request: The request from the client 
    : return: The parsed request.
    """

    cleaned_request = {
        'id': str(uuid.uuid4()),
        'title': request.get('title'),
        'description': request.get('description'),
        'due_date': request.get('due_date'),
        'completed': request.get('completed'),
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),

    }

    return cleaned_request


def save_todo(todo: Dict, todo_list: List) -> NoReturn:
    """
    save the todo to the list
    :param todo: the todo to save.
    :param todo_list: the list to save the todo to.
    :return:
    """
    todo_list.append(todo)
