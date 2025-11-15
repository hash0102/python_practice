from typing import TypeVar, List

T = TypeVar('T')  # 型変数Tを定義

def first_element(lst: List[T]) -> T:
    return lst[0]

# intを指定知れば型変数Tはintになる
print(first_element([1, 2, 3]))       # 出力: 1 （int型）
# strを指定知れば型変数Tはstrになる
print(first_element(['a', 'b', 'c'])) # 出力: 'a' （str型）
