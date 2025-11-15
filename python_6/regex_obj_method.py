import re

# match
pattern = re.compile(r"\d+")
result = pattern.match("123abc")
print(result.group())  # '123'

# 途中に数字があっても、先頭にないとマッチしない：
print(pattern.match("abc123"))  # None

# search
result = pattern.search("abc123def")
print(result.group())  # '123'

# 途中に数字があってもマッチ
print(pattern.search("abc123").group())

# findall
result2 = pattern.findall("abc123def456")
print(result2)  # ['123', '456']

# finditer
for m in pattern.finditer("abc123def456"):
    print(m.group())
# 出力:
# 123
# 456

# sub
pattern = re.compile(r"\d+")
result3 = pattern.sub("###", "abc123def456")
print(result3)  # abc###def###

# fullmatch
pattern = re.compile(r"\d+")
print(pattern.fullmatch("123"))     # マッチ
print(pattern.fullmatch("123abc"))  # None（全体が一致しない）
