import re

# groups
pattern = re.compile(r"(\d{2})-(\d{4})-(\d{4})")
match = pattern.search("電話: 03-1234-5678")

print(match.groups())
# 出力: ('03', '1234', '5678')

# groupdict
pattern = re.compile(r"(?P<area>\d{2})-(?P<number1>\d{4})-(?P<number2>\d{4})")
match = pattern.search("電話: 03-1234-5678")

print(match.groupdict())
# 出力: {'area': '03', 'number1': '1234', 'number2': '5678'}

# expand
pattern = re.compile(r"(?P<area>\d{2})-(?P<number1>\d{4})-(?P<number2>\d{4})")
match = pattern.search("電話: 03-1234-5678")

print(match.expand(r"市外局番: \g<area>, 番号: \g<number1>-\g<number2>"))
# 出力: 市外局番: 03, 番号: 1234-5678



