import datetime

import requests

BASE_URL = "http://127.0.0.1:5000/"

login_args = {
    'user_id': 4,
    'name': 'Jingshi Liu',
    'email': 'jingshiliu@email.com',
    'password': '12456'
}

print(requests.post(BASE_URL + 'user', json=login_args).json())

create_log_args = {
    'user_id': 4,
    'date': datetime.datetime.now().strftime('%b %d %Y %H %m %S'),
    'data': 'I am data!'
}
print(create_log_args['date'])

print(requests.post(BASE_URL + 'log', json=create_log_args).json())

get_logs_args = {
    'user_id': 4,
}
print(requests.get(BASE_URL + 'log', json=get_logs_args).json())


setting_post_args = {
    'user_id': 4,
    'data': 'i am dateeee'
}


print(requests.get(BASE_URL + 'settings', json=setting_post_args).json())

