a = 2
b = 3

# 位置引数の場所を指定
print('{1} * {0} = {2}'.format(a, b, a*b))

# キーワード引数
print('{a} * {b} = {c}'.format(a=a, b=b, c=a*b))

# {}を書いた順と位置引数の順番が一致するように値が埋め込まれる
print('{} * {} = {}'.format(a, b, a*b))