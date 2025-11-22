from collections import OrderedDict

od = OrderedDict()
od['apple'] = 3
od['banana'] = 2
od['cherry'] = 5

# 追加した順番と同じ順（順序を保持して）出力
print(od)
# → OrderedDict([('apple', 3), ('banana', 2), ('cherry', 5)])
print('----------------------------------')

# move_to_end()
od2 = OrderedDict({'a': 1, 'b': 2, 'c': 3})
# aを最後にする(last引数を指定しない)
od2.move_to_end('a')
print(od2)  # → OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# cを先頭にする
od2.move_to_end('c', last=False)
print(od2)  # → OrderedDict([('c', 3), ('b', 2), ('a', 1)])
print('----------------------------------')

# popitem()
# 最後の要素を取り出す
od3 = OrderedDict({'a': 1, 'b': 2, 'c': 3})
od3.popitem()         # → ('c', 3)
print(od3)
# 最初の要素を取り出す
od4 = OrderedDict({'a': 1, 'b': 2, 'c': 3})
od4.popitem(last=False)  # → ('a', 1)
print(od4)
print('----------------------------------')
