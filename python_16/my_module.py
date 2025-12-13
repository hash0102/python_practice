import requests

def get_data():
    response = requests.get('http://example.com/api')
    return response.status_code


def my_function(num:int):
    return num * 2