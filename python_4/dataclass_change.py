from dataclasses import dataclass, asdict, astuple

# クラスデコレーターでdataclassを宣言
@dataclass
class User:
    # クラス変数を宣言、型ヒントを宣言
    name: str
    age: int
    address: str

user =User('bob',34,'Miami')


print(user)
print(astuple(user))
print(asdict(user))