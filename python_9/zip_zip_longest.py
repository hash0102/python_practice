# zip
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]
print(list(zip(names, scores)))

# 長さが違うイテラブルの場合
names = ['Alice', 'Bob']
scores = [85, 90, 95]

print(list(zip(names, scores)))
# → [('Alice', 85), ('Bob', 90)] ← 短い方で打ち切り

# zip_longest
from itertools import zip_longest

names = ['Alice', 'Bob']
scores = [85, 90, 95]

# 足りない値を「-」で埋める
print(list(zip_longest(names, scores, fillvalue='-')))