from io import BytesIO

# BytesIOのインスタンス生成
b = BytesIO(b"abc")  # 初期値あり
print(b.getvalue())
b2 = BytesIO()       # 空で作成
print(b2.getvalue())
print('----------------------------------')

# write
b3 = BytesIO()
print(b3.write(b"Hello"))        # 5
print(b3.write(b" World"))        # 6
print(b3.getvalue())       # b'Hello World'
print('----------------------------------')

# read
b4 = BytesIO(b"ABCDEFG")
print(b4.read(3))   # b'ABC'
print(b4.read())    # b'DEFG'
print('----------------------------------')

# tell
b5 = BytesIO(b"xyz")
b5.read(2)
print(b5.tell())    # 2
print('----------------------------------')

# seek
b6 = BytesIO(b"Hello World")
b6.seek(6)             # カーソルを "World" の先頭に
print(b6.read())       # b'World'
print('----------------------------------')

# getvalue
b7 = BytesIO()
b7.write(b"abc")
print(b7.getvalue())  # b'abc'
print('----------------------------------')

# getbuffer
b7 = BytesIO(b"abcde")
buf = b7.getbuffer()
print(type(buf))
print(buf[1])        # 98 (b)
buf[1] = 90          # b -> Z
print(b7.getvalue())  # b'aZcde'

# close
b8 = BytesIO(b"xyz")
b8.close()
# b8.read()  → ValueError: I/O operation on closed file.