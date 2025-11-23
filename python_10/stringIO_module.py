from io import StringIO

# StringIoクラスのインスタンス生成
buffer = StringIO("初期文字列")
print(type(buffer))
print('----------------------------------')

# write
buffer2 = StringIO()
res = buffer2.write("Hello")
# 戻り値
print(res)
buffer2.write(" World")
print(buffer2.getvalue())  # 'Hello World'
print('----------------------------------')

# read
buffer3 = StringIO("Hello World")
print(buffer3.read(3))     # 'Hel'
print(buffer3.read())      # 'lo World'
print('----------------------------------')

# seek
buffer4 = StringIO("Hello World")
buffer4.seek(6)         # 'World' にカーソル移動
print(buffer4.read())   # 'World'
print('----------------------------------')

# tell
buffer5 = StringIO("Hello")
#　初期カーソルなので0
print(buffer5.tell())
# 3文字read
print(buffer5.read(3))
# ３文字移動したので3
print(buffer5.tell())  # 3
print('----------------------------------')

# getvalue
buffer6 = StringIO()
buffer6.write("abc")
buffer6.seek(0)
print(buffer6.read(1))
# readやseekに影響されず全体を返す
print(buffer6.getvalue())  # 'abc'
print('----------------------------------')

# close
buffer7 = StringIO("abc")
buffer7.close()
# buffer.write("x")  → ValueError: I/O operation on closed file
