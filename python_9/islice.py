from itertools import islice

data = ['a', 'b', 'c', 'd', 'e']
# インデックスの1~4番目を抽出
result = islice(data, 1, 4)
print(list(result))  # ['b', 'c', 'd']
# 以下と同じ意味
print(data[1:4])
print('----------------------------------')

# イテレータに対して使う
def numbers():
    n = 0
    while True:
        yield n
        n += 1

# 無限イテレータから最初の10個だけ取り出す
# 通常のsliceはイテレーターには使えない
for i in islice(numbers(), 10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print('')
print('----------------------------------')

# ステップを指定する
data = range(20)
# インデックスの2~15の間を3つの感覚で抽出
result = islice(data, 2, 15, 3)
print(list(result))  # [2, 5, 8, 11, 14]