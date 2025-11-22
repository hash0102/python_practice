# 文字列の長さで並び替え
words = ['banana', 'kiwi', 'apple']
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['kiwi', 'apple', 'banana']
print('----------------------------------')

# 辞書のリストを、あるキーの値で並び替え
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# 年齢順に並べ替え
# lambda person: person['age'] という無名関数が、各要素から「年齢」を取り出してソート基準にしている。
sorted_people = sorted(people, key=lambda person: person['age'])

for p in sorted_people:
    print(p['name'], p['age'])
print('----------------------------------')