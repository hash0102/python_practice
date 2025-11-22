numbers = [3, 1, 4, 1, 5]
res = numbers.sort()
# 戻り値はNone
print(res)

print(numbers)  # [1, 1, 3, 4, 5]
print('----------------------------------')

# 長さで並べ替え（文字列）
words = ['banana', 'kiwi', 'apple']
words.sort(key=len)
print(words)  # ['kiwi', 'apple', 'banana']
print('----------------------------------')

# 降順に並べ替え
numbers = [3, 1, 4, 1, 5]
numbers.sort(reverse=True)
print(numbers)  # [5, 4, 3, 1, 1]
print('----------------------------------')

# reversed
a = [1, 2, 3]
res2 = a.reverse()
# 戻り値はNone
print(res)
print(a)  # [3, 2, 1]
print('----------------------------------')