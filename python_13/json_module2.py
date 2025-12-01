import json

# load
with open('data.json', 'r') as f:
    # jsonファイルをload
    python_dict = json.load(f)
print(python_dict)
print(type(python_dict))
print('-' * 30)

# dump
python_dict = {
    "name": "Bob",
    "age": 25,
    "city": "Osaka"
}

# Pythonの辞書をdata2.jsonに書き込む
with open('data2.json', 'w') as f:
    json.dump(python_dict, f, indent=4)