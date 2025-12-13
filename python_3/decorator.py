# デコレーター関数
def my_decorator(func):
    def wrapper():
        print("関数が呼ばれる前の処理")
        func()
        print("関数が呼ばれた後の処理")
    return wrapper

# デコレーターを使用
@my_decorator
def hello():
    print("Hello!")

hello()
print('-' * 30)

# 関数にretryデコレーターを適用
import random
from retrying import retry

@retry
def my_func():
    if random.randint(0, 10) == 5:
        print('5')
    else:
        print('raise ValuError')
        raise ValueError("not 5")

my_func()
print('-' * 30)

def init_logger(cls):
    orig_init = cls.__init__
    def new_init(self, *args, **kwargs):
        print("_init__の引数：", *args)
        print(f"{cls.__name__} を初期化します")
        orig_init(self, *args, **kwargs)
    # __init__ をラップ
    cls.__init__ = new_init
    # 受け取ったclassを返す
    return cls

# classにデコレーターを適用
@init_logger
class Person:
    def __init__(self, name):
        self.name = name

# インスタンス生成
p = Person("Alice")
print('-' * 30)

# 2つ以上のデコレーターを適用
import time
from functools import wraps

# timer が先に関数をラップ
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.5f} seconds")
        return result
    return wrapper

# その結果を logger がさらにラップ
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 実行時の順序は logger → timer → slow_task
@logger
@timer
def slow_task(n):
    """n秒待つだけの処理"""
    time.sleep(n)
    return "done"

print(slow_task(1))
print('-'*30)

# 関数内に関数を定義する
def func_greeting(name):
    # 関数の中に関数を定義できる
    def print_greeting():
        print(f'こんにちは{name}')
    # 関数を返せる
    return print_greeting

func = func_greeting('john')
print(func)
func()
print('-'*30)

# 関数を別の関数の引数として与える
def after_greeting(func, name):
    func(name)
    print('aiueo')

def greeting(name):
    print(F'hello,{name}')

after_greeting(greeting, 'john')
print('-'*30)

# デコレーター関数を作成し代入文を使用

# デコレーター関数
def my_decorator(func):
    # デコレート対象の関数の代わりに呼び出されるラッパー関数
    def wrap_function():
        func()
        print(F'function:{func.__name__} called')
    return wrap_function


def greeting():
    print('Hello')

# （１）デコレート構文と等価である代入文を使用
greeting = my_decorator(greeting)
greeting
greeting()
print('-'*30)

# 上記のサンプルコード（１）の箇所を「@デコレーター名」の構文を使用して置き換え
@my_decorator
def greeting():
    print('Hello')

greeting
greeting()
print('-'*30)

# デコレーターの使用により元の関数名が失われる
def my_decorator2(func):
    def wrap_function(a):
        """wrap_functionのドキュメント"""
        func(a)
    return wrap_function

@my_decorator2
def greeting(name):
    """greetingのドキュメント"""
    print(F'Hello, {name}')

print(greeting)
# gteetingの名前がwrap_functionになっている
print(greeting.__name__)
# ドキュメントの内容がwrap_functionになっている
print(greeting.__doc__)

print('-'*30)

# functools.wrapsを使用
from functools import wraps

def my_decorator3(func):
    # この１行を追加
    @wraps(func)
    def wrap_function(a):
        """wrap_functionのドキュメント"""
        func(a)
    return wrap_function

@my_decorator3
def greeting(name):
    """greetingのドキュメント"""
    print(F'Hello, {name}')

print(greeting)
print(greeting.__name__)
print(greeting.__doc__)
