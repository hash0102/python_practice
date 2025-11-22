numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 5, 9]
print('----------------------------------')

# 元のリストは変わらない
print(numbers)  # [5, 2, 9, 1]
print('----------------------------------')

# reverse=True
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # [9, 5, 2, 1]
print('----------------------------------')

# key を使う（並び替えのルールを指定）
words = ['apple', 'banana', 'kiwi']
# 文字列の長さの昇順でソート
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['kiwi', 'apple', 'banana']
print('----------------------------------')

# 辞書のリストを、あるキーの値でソート
people = [{'name': 'Alice', 'age': 30},
          {'name': 'Bob', 'age': 25},
          {'name': 'Charlie', 'age': 35}]
# ageの値の昇順でソート
sorted_people = sorted(people, key=lambda x: x['age'])
print(sorted_people)
print('----------------------------------')