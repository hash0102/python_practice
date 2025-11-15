from typing import TypedDict

class BookDict(TypedDict):
    name: str
    author: str
    price: int

fav_book: BookDict = {"name": "start", "author": "Bob", "price": int}