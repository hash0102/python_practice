# id
i= 'aiueo'
print(id(i))

list_ex = []
print(id(list_ex))
list_ex.append('aiueo')
# listが同じオブジェクトのため、値を追加しても同じIdが表示される
print(id(list_ex))

# type
print(type(1))
print(type("test"))
print(type([]))

# isinstance
print(isinstance(1, int))
print(isinstance(1, str))
# 複数のデータ型のいずれかに属しているかのチェックは、第２引数をタプルで渡す
print(isinstance([], (tuple,list)))
print(isinstance("1.0", (int, float)))

# このチェックは継承元も含めて確認される。
print(isinstance(True, bool))

# bool型はint型を継承している。
print(isinstance(True, int))
print(isinstance(True, float))

# Pythonのオブジェクトはすべて親クラスであるobjectを継承している
print(isinstance(1, object))
def func():
    pass
print(isinstance(func, object))

# issubclass
print(issubclass(bool,int))
print(issubclass(bool,float))
print(issubclass(bool, object))

# help
help(int)

def func():
    """関数のdocstring"""
    pass

help(func)

#dir
# 文字列の例
print(dir("test"))