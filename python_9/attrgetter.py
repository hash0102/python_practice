# Person オブジェクトの age 属性でソート
from operator import attrgetter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person('Alice', 30),
    Person('Bob', 20),
    Person('Charlie', 35)
]

# age属性でソート
sorted_people = sorted(people, key=attrgetter('age'))

print([p.name for p in sorted_people])
# ['Bob', 'Alice', 'Charlie']
print('----------------------------------')

# itemgetter / attrgetter は 複数キー も扱える
people2 = [
    Person('Alice', 30),
    Person('Bob', 30),
    Person('Charlie', 35)
]
# 年齢 → 名前の順にソート
sorted_people2 = sorted(people2, key=attrgetter('age', 'name'))
print([p.name for p in sorted_people2])