# ０～９を２乗したリストを作成する処理

# 普通の処理
num_list = []
for i in range(10):
    num_list.append(i**2)
print(num_list)

# 内包表記
num_list2 = []
num_list2 = [i**2 for i in range(10)]
print(num_list2)

# 要素をフィルタリングしたい場合は、if文を使用する
# 偶数のみリストに追加
num_list3 = [i**2 for i in range(10) if i % 2 == 0]
print(num_list3)

print('-' * 30)

# ネストしたリストの内包表記
drinks = ['coffee','tea','moka']
sizes = ['S', 'M', 'L']

# 普通の処理
menu = []
for drink in drinks:
    for size in sizes:
        menu.append((drink, size))
print(menu)

# 内包表記
menu2 = [(drink, size) for drink in drinks for size in sizes]
print(menu2)

print('-' * 30)

# 集合内包表記
num_list4 = {i**2 for i in range(10) if i % 2 == 0}
print(num_list4)
print(type(num_list4))
print('-' * 30)

# 辞書内包表記
# keyがn、valueがnの2乗の辞書を作成
num_list5 = {i: i**2 for i in range(5)}
print(num_list5)
print(type(num_list5))
print('-' * 30)

# ジェネレーター式
# for文で値を返す時にi**2の結果が作成される。
g = (i**2 for i in range(5))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))