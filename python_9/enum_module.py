from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 1

# 定数を呼び出す
print(Color.RED)       # Color.RED（列挙型の名前）
print(Color.RED.name)  # 'RED'（定数名）
print(Color.RED.value) # 1（定数に割り当てた値）
print('----------------------------------')

# 逆引き（値 → Enum）も可能
print(Color(1))  # Color.RED

# 比較
# 同じクラスの同じ値なのでTrue
print(Color.RED == Color.YELLOW)

# 値が違うのでFalse
print(Color.RED == Color.BLUE)

class Shape(Enum):
    CIRCLE = 1

# クラスが違うのでFalse
print(Color.RED == Shape.CIRCLE)

# 列挙型以外なのでFalse
print(Color.RED == 1)