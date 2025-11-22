from itertools import chain

a = [1, 2, 3]
b = [4, 5]
c = [6]

# chain
result = chain(a, b, c)
print(type(result))
print(list(result))  # → [1, 2, 3, 4, 5, 6]
print('----------------------------------')

# 文字列の配列と文字列も連結可能
d = ['a','b']
e = ['c']
f = 'defg'
result2 = chain(d,e,f)
print(list(result2))
print('----------------------------------')

# 文字列と数字の配列の連結も可能
g = ['h','i']
h = ['j']
i = [1234]
result3 = chain(g,h,i)
print(list(result3))
print('----------------------------------')

# 文字列や辞書キーなども対象にできる
for ch in chain("ABC", "123"):
    print(ch, end=" ")  # A B C 1 2 3
print('')
print('----------------------------------')