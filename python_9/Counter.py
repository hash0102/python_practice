from collections import Counter

# 文字列の中の各文字の出現回数をカウント
c = Counter("banana")
# Counterオブジェクトを返す
print(type(c))
print(c)
print('----------------------------------')

# リストでも使える
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(fruits)
print(counter)
print('----------------------------------')

# elements
c = Counter({'a': 3, 'b': 1, 'c': 0, 'd': -2})
print(list(c.elements()))
print('----------------------------------')

# most_common
c = Counter("abracadabra")
# すべての多い順を返す
print(c.most_common())
# 上位３つの要素の多い順を返す
print(c.most_common(3))
print('----------------------------------')

# subtract
c = Counter(a=4, b=2, c=0)
# aから1、bから3、cから2、dから1を引く（値がない場合はマイナス）
c.subtract({'a': 1, 'b': 3, 'c': 2, 'd': 1})
print(c)
print('----------------------------------')

# update
c2 = Counter({'a': 1, 'b': 2})
# aに2、bに1、cに3を足す
c2.update({'a': 2, 'b': 1, 'c': 3})
print(c2)
print('----------------------------------')

c3 = Counter(a=3, b=1, d=-1)
c4 = Counter(a=1, b=2, c=3)
#  加算（０以下は除外）
print(c3 + c4)
# 減算(０以下は除外)
print(c3 - c4)
# 積（共通するキーだけ取り出し、小さい方の値をとる）
print(c3 & c4)
# 和集合（両方のキーのうち、大きい方の値をとる）
print(c3 | c4)