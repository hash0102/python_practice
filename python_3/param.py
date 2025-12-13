# 位置引数
def sample_func(param1, param2, param3):
    print(f'{param1}, {param2}, {param3}')

sample_func('egg','cheese','tomato')
print('-'*30)

# キーワード引数
def sample_func(param1, param2, param3):
    print(f'{param1}, {param2}, {param3}')

sample_func(param3='egg',param2='cheese',param1='tomato')
print('-'*30)

# 位置引数とキーワード引数の混在
def sample_func(param1, param2, param3):
    print(f'{param1}, {param2}, {param3}')

# 位置引数を先、キーワード引数を後に指定
sample_func('egg',param3='cheese',param2='tomato')
print('-'*30)

# キーワード引数の後ろに位置引数を置くとエラー
# sample_func(param3='tomato', 'egg', 'cheese')

# 位置引数としてtomatoがparam1に渡されているが、eggもparam1に指定しているためエラー
# sample_func('tomato', 'cheese', param1='egg') 

# デフォルト値付き引数
def sample_func(param1, param2=2, param3=3): # param2、param3にデフォルト値を設定
    print(f'{param1}, {param2}, {param3}')

# 必須の引数のみ与える
sample_func(1) 

# 1つのオプション引数を与える
sample_func(1,20) 

sample_func(1, param3='hoge')

# すべての引数を与える
sample_func(10, 20, 30) 

print('-'*30)

# 可変長位置引数
def func_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

func_sum(1, 2, 3, 4, 5)

# リストやタプルの要素を可変長引数として渡す
num = [1, 2, 3, 4, 5]
func_sum(*num)

num = (1, 2, 3, 4, 5)
func_sum(*num)

# 可変長位置引数の定義位置
def sample_func(param1, param2, *args):
    print(F'{param1},{param2},{args}')

# param1に1、param2に2、argsに3,4,5が渡される。
sample_func(1,2,3,4,5)
print('-'*30)

def sample_func2(param1, default_arg=0, *args):
    print(F'{param1},{default_arg},{args}')

# エラー
# sample_func2(1, default_arg=10, 2, 3, 4, 5)

# エラー
# sample_func2(1, 2, 3, 4, 5, default_arg=10)

# 可能だが可読性が下がる
sample_func2(1, 10, 2, 3, 4, 5)
print('-'*30)

# 可変長キーワード引数
def sample_func(name, **kwargs):
    print(name)
    for key, value in kwargs.items():
        print(F'{key}: {value}')

sample_func('john', age=30, email='hoge@hoge.com')

# 辞書の各キーと値を複数のキーワード引数として関数に渡す場合は「**」をその辞書の前につけて渡す
user_dict = {'name': 'john', 'age': 30, 'email': 'hoge@hige.com'}
sample_func(**user_dict)
print('-'*30)

# キーワード専用引数
def sample_func(param1, *, keyword1):
    print(param1)
    print(keyword1)

sample_func(1, keyword1=False)
print('-'*30)

# キーワード引数として渡していないのでエラー
# sample_func(1, False)

# 位置専用引数
def add(x, y, /):
    print(x + y)

add(1,2)

# キーワード引数として呼び出そうとするとエラー
# add(x=1, y=2)