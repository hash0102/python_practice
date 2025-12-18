class MyObject:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'__str__: {self.name}'
    
    def __repr__(self):
        return f'__repr__: {self.name}'

# printなので__str__が実行
print( MyObject('test'))

# __repr__はスクリプト実行では呼ばれない
# REPL（対話環境）では __repr__ が呼ばれる
MyObject(name='test')