from typing import Union

# Union
def address_code(number: Union[int, str]) -> int:
    pass

your_code: int = address_code(100000)
me_code: int = address_code("20000")

# 3.10以降の場合
def address_code(number: int | str) -> int:
    pass

your_code: int = address_code(100000)
me_code: int = address_code("20000")

# Optional
from typing import Optional

price: Optional[int]

# Literal
from typing import Literal

FILETYPE = Literal["csv", "json", "xml"]
def access_file(file: str, file_type: FILETYPE):
    pass

access_file("whether.csv", "csv")

#htmlは含まれないためNG 
access_file("wheather.html", "html")

# Any
from typing import Any

# 関数の引数や戻り値にAnyを指定
def process_by_type(user_input: Any) -> Any:
    if isinstance(user_input, str):
        pass