from operator import itemgetter

people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# オブジェクトの'age'の要素を取り出し、ソート
sorted_people = sorted(people, key=itemgetter('age'))

print([p['name'] for p in sorted_people])
# ['Bob', 'Alice', 'Charlie']
print('----------------------------------')

# タプルのリストを第2要素でソート
from operator import itemgetter

data = [('apple', 3), ('banana', 1), ('kiwi', 2)]
# インデックス番号の１の値でソート
sorted_data = sorted(data, key=itemgetter(1))
print(sorted_data)
# [('banana', 1), ('kiwi', 2), ('apple', 3)]
print('----------------------------------')