import datetime

import requests

BASE_URL = "http://127.0.0.1:5000/"

login_args = {
    'user_id': 4,
    'name': 'Jingshi Liu',
    'email': 'jingshiliu@email.com',
    'password': '123456'
}

print(requests.post(BASE_URL + 'user', json=login_args).json())

create_log_args = {
    'user_id': 2,
    'date': datetime.datetime.now().strftime('%b %d %Y %H'),
    'data': 'I am data!'
}

# print(requests.post(BASE_URL + 'log', json=create_log_args).json())

get_logs_args = {
    'user_id': 2,
}
# print(requests.get(BASE_URL + 'log', json=get_logs_args).json())

