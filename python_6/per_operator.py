# 文字列の埋め込みは「%s」を使う
print('Hello, %s!' %'Taro')

# 整数の埋め込みは「%d」を使う
print('1 + 3 = %d' % 4)

# 複数の値を埋め込む場合はタプルで指定
a = 2
b = 3
print(' %d * %d = %d' % (a, b, a*b))

# 辞書型も使用可能
print('%(name)s likes %(lang)s' % {'name': 'Taro', 'lang': 'Python'})