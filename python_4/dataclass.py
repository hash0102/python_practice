# frozen引数を設定し、データ変更ができないdataclassを宣言
@dataclass(frozen=True)
class FrozenUser:
    name: str
    age: int
    address: str