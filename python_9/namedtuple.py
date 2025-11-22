from collections import namedtuple

# クラスの定義（Personという名前のnamedtuple）
Person = namedtuple('Person', ['name', 'age'])

# インスタンス生成
p = Person(name='Alice', age=30)

# フィールドアクセス
print(p.name)  # Alice
print(p.age)   # 30

# タプルとしても使える
print(p[0])    # Alice
print(p[1])    # 30
print('----------------------------------')

# _replace
p2 = p._replace(age=31)
print(p2)  # Person(name='Alice', age=31)
# 元は変更されない
print(p)
print('----------------------------------')

# _asdict
print(p._asdict())  # {'name': 'Alice', 'age': 30}
print('----------------------------------')

# _fields
print(p._fields)  # ('name', 'age')
print('----------------------------------')

# フィールド名を文字列で指定する方法
# name、department、salaryのフィールド名を指定
Employee = namedtuple('Employee', 'name department salary')
e = Employee('Bob', 'Sales', 50000)
print(e.department)  # Sales
print('----------------------------------')