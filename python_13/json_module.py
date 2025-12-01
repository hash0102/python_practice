import json

# 辞書
python_dict = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "History"]
}

# dumps
# Pythonの辞書をJSON形式の文字列に変換
json_string = json.dumps(python_dict)
print(json_string) 
print(type(json_string))
print('-' * 30)

# 読みやすくするためにインデントを設定
json_formatted_string = json.dumps(python_dict, indent=4)
print(json_formatted_string)
print(type(json_string))
print('-' * 30)

json_string2 = '{"name": "Alice", "age": 30, "is_student": false, "courses": ["Math", "History"]}'

# loads
# JSON形式の文字列をPythonの辞書に変換
python_dict2 = json.loads(json_string2)
print(python_dict2)
print(type(python_dict2))
print('-' * 30)

# Pythonの辞書なので、キーを使って値にアクセスできる
print(python_dict2['name'])
print(type(python_dict2['name']))
print('-' * 30)

# object_hook
def convert_to_user_object(data):
    # 'name'キーが存在する場合のみ、Userクラスのインスタンスに変換
    if 'name' in data:
        print(f"Hooking object: {data['name']}")
        return User(data['name'], data['age'])
    return data

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"User(name='{self.name}', age={self.age})"

json_string3 = '{"name": "Bob", "age": 25}'
# object_hookにconvert_to_user_object関数を指定
user_instance = json.loads(json_string3, object_hook=convert_to_user_object)

print(user_instance)
print(type(user_instance)) 
print('-' * 30)

# object_paris_hook
import json
from collections import OrderedDict

# キーの挿入順序を保持する OrderedDict に変換
json_string4 = '{"a": 1, "c": 3, "b": 2}'
ordered_dict = json.loads(json_string4, object_pairs_hook=OrderedDict)

print(list(ordered_dict.keys()))
print(type(ordered_dict))