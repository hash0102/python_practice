nums = [1, 2, 3, 4]
rev = reversed(nums)
# list_reverseiteratorオブジェクトが返る
print(type(rev))
print(list(rev))  # [4, 3, 2, 1]
print('----------------------------------')

# 文字列でも使える
s = "hello"
rev = reversed(s)
print("".join(rev))  # "olleh"
print('----------------------------------')

# タプルや range にも使える
t = (10, 20, 30)
print(tuple(reversed(t)))  # (30, 20, 10)

r = range(5)
print(list(reversed(r)))   # [4, 3, 2, 1, 0]