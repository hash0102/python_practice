from collections import defaultdict

# int関数を使う（デフォルトは 0）
count = defaultdict(int)
count['apple'] += 1
count['banana'] += 1
print(count)  # → defaultdict(<class 'int'>, {'apple': 1, 'banana': 1})
print('----------------------------------')

# listを使う（デフォルトは []）
grouped = defaultdict(list)
grouped['fruit'].append('apple')
grouped['fruit'].append('banana')
grouped['veggie'].append('carrot')
print(grouped)
# → defaultdict(<class 'list'>, {'fruit': ['apple', 'banana'], 'veggie': ['carrot']})
print('----------------------------------')

# strを使う（デフォルトは ''）
text = defaultdict(str)
text['greeting'] += "Hello, "
text['greeting'] += "World!"
print(text['greeting'])  # → Hello, World!
print('----------------------------------')

# カスタム初期値（関数で定義も可）
def default_zero():
    return 0

d = defaultdict(default_zero)
d['x'] += 5
print(d['x'])  # → 5
