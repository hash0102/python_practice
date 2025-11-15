# タプルのすべての要素に型付けしているためOK
hobby: tuple[str, str] = ("game", "manga")

# すべての要素に対して型付けしていないためNG
hobby_err: tuple[str] = ("game", "manga")

# 同じ型の要素を持つタプル
hobby_many: tuple[str, ...] = ("game","manga", "book")

from dataclasses import dataclass

@dataclass
class Book:
    name: str
    author: str
    price: int

example = Book("saw", "bob", 2500)