# タプルのアンパック
tp = (1, 2, 3)
a, b, c = tp
print(F'{a}, {b}, {c}')

# タプルは（）が省略可能
d, e, f = 4, 5, 6
print(F'{d}, {e}, {f}')

# リストも同様
lt = [1, 2, 3]
a, b, c = lt
print(F'{a}, {b}, {c}')

my_dict = {'a': 1, 'b': 2, 'c': 3}
# 辞書のキーをアンパック
key1, key2, key3 = my_dict
print(F'{key1}, {key2}, {key3}')

# 辞書の値をアンパック
v1, v2, v3 = my_dict.values()
print(F'{v1}, {v2}, {v3}')

# 変数の数が一致しないとエラー
try:
    a, b, c = 1, 2
except Exception as e:
    print(e)
    pass
print('-' * 30)

# ネストしたタプル、リストのアンパック
tp = (0, 1, (2, 3, 4))
a, b, c = tp
print(F'{a}, {b}, {c}')

a, b, (c, d, e) = tp
print(F'{a}, {b}, {c}, {d}, {e}')
print('-' * 30)

# アスタリスクを使ったアンパック
tp = (0, 1, 2, 3, 4)
a, b, *c = tp
print(F'{a}, {b}, {c}')

a, *b, c = tp
print(F'{a}, {b}, {c}')

*a, b, c = tp
print(F'{a}, {b}, {c}')

# 2つ以上つけるとエラー
# *a, *b, c = tp
print('-' * 30)

# 関数の引数のアンパック
def sample_func(param1, param2, param3):
    print(F'{param1}, {param2}, {param3}')

args = [1, 2, 3]
# [1, 2, 3]を展開して仮引数に渡している
sample_func(*args)