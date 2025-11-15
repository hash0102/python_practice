from shared import exe_func

# 文字列が数字と文字列の場合のみにTrueを返すメソッド「isalnum()」
exe_func("123aaa","123aaa".isalnum)

# 記号があるためエラー
exe_func("123###","123###".isalnum)

# 文字列が文字のみの場合（日本語含む）にTrueを返すメソッド「isaipha()」
exe_func("Bobあああ","Bobあああ".isalpha)

# 文字列が十進数字を表す場合にTrueを返すメソッド「isdecimal()」
exe_func("10","10".isdecimal)

# 文字列が数字を表す文字のみにTrueを返すメソッド「isdigit()」
exe_func("123","123".isdigit)

# 識別子として使用できる文字列の場合にTrueを返すメソッド「isidentifier()」
exe_func("aaa","aaa".isidentifier)

# 文字列がすべて小文字の場合にTrueを返すメソッド「islower()」
exe_func("aaa","aaa".islower)

# 数を表す文字列（漢数字も含む）の場合にTrueを返すメソッド「isnumeric()」
exe_func("123", "123".isnumeric)

# 印字可能な文字列の場合にTrueを返すメソッド「isprintable()」
exe_func("aaa","aaa".isprintable)

# 制御文字があるとエラー
exe_func("aaa\nbbb","aaa\nbbb".isprintable)

# スペース・タブなどの空文字の場合にTrueを返すメソッド「isspace()」
exe_func(" "," ".isspace)

# 文字列が先頭のみが大文字であとは小文字の場合にTrueを返すメソッド「istitle()」
exe_func("Apple","Apple".istitle)

# 文字列がすべて大文字の場合にTrueを返すメソッド「isupper()」
exe_func("APPLE","APPLE".isupper)