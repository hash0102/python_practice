# open()
with open('python.txt') as f:
    print(f.read())
    print(dir(f))
print('-'*30)

# with文を使用しない場合
f = None
try:
    f = open('python.txt')
    print(f.read())
    print(dir(f))
finally:
    if f:
        f.close()
print('-'*30)

# コンテキストマネージャー
class MyOpenContextManager:
    def __init__(self, file_name):
        self.file_name = file_name
    def __enter__(self):
        print('__enter__：ファイルを開きます')
        self.file_obj = open(self.file_name, 'r')
        return self.file_obj # __enter__で返したオブジェクトはasで参照できる
    def __exit__(self , type, value, traceback):
        print({type})
        print({value})
        print({traceback})
        print('__exit__：ファイルを閉じます')
        self.file_obj.close()

with MyOpenContextManager('python.txt') as f:
    print(f.read())
    print(dir(f))
print('-'*30)

# @contextlib.contextmanager
import contextlib
import traceback

@contextlib.contextmanager
def my_open_context_manager(file_name):
    file_obj = open(file_name, 'r')
    try:
        print('file open')
        yield file_obj
    except Exception as e:
        print(e)
        print(list(traceback.TracebackException.from_exception(e).format()))
        raise
    finally:
        file_obj.close()
        print('file close')

with my_open_context_manager('python.txt') as f:
    print(f.read())
print('-'*30)


import contextlib
import os

# contextlib.suppressの例
with contextlib.suppress(FileNotFoundError):
    os.remove('sample.txt') # ファイルが存在しない場合、通常はエラーになるが、エラーが無視される

# contextlib.redirect_stdoutの例
with open('sample.log', 'w') as f:
    with contextlib.redirect_stdout(f):
        print('log write') # print()は標準出力されるが、ファイルに書き出すことができる