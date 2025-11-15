import re
from shared import re_result

match = re.search(r"\d+", "abc123xyz")
if match:
    print(match.group())  # → '123'
# \d+ は「1文字以上の数字」
# search() は最初にマッチした部分を返す
# group() はそのマッチ文字列（この場合は '123'）を返す

# group
match = re.search(r"(\d+)-(\d+)", "電話: 03-1234")
print(match.group())   # '03-1234'
print(match.group(0))  # 同じ → '03-1234'

print(match.group(1))  # '03'（最初の括弧）
print(match.group(2))  # '1234'（2番目の括弧）

# 複数グループを一度に取得したい場合
print(match.groups())  # タプルで返る → ('03', '1234')

# 名前付きグループ
pattern = re.compile(r"(?P<area>\d{2})-(?P<number1>\d{4})-(?P<number2>\d{4})")
text = "電話: 03-1234-5678"

match = pattern.search(text)

if match:
    # 名前で取得
    print(match.group("area"))
    print(match.group("number1"))
    print(match.group("number2")) 