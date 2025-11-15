from shared import exe_func

# 文字列をすべて大文字に変換するメソッド「upper()」
exe_func("abc","abc".upper)

# 文字列をすべて小文字に変換するメソッド「lower()」
exe_func("ABC","ABC".lower)

# 大文字を小文字に、小文字を大文字に変換するメソッド「swapcase()」
exe_func("ABCdef","ABCdef".swapcase)

# 先頭1文字を大文字に、それ以外を小文字に変換するメソッド「capitalize()」
exe_func("hELLO","hELLO".capitalize)

# 単語ごとに「大文字１文字＋小文字」の形式に変換するメソッド「title()」
exe_func("HELLO, bob, MIKE","HELLO, bob, MIKE".title)

# 第一引数を第二引数に変換した文字列を返すメソッド「replace()」
variable = "Hi, Bob , Hi, Mike"
exe_func(variable,variable.replace,"Hi", "Hello")

# 第三引数に数字を指定でき、先頭から指定した数だけ変換する
exe_func(variable,variable.replace,"Hi", "Hello",1)

# 文字列の先頭及び末尾から指定した文字をすべて除去するメソッド「strip([chars])」
# chars はオプション：除去したい文字（複数指定可）
# デフォルトでは、**前後の空白文字（スペース・タブ・改行など）**を除去
exe_func("aaa/bbb/aaa/ccc/bbb/ddd/bbb","aaa/bbb/aaa/ccc/bbb/ddd/bbb".strip,"ab")

# 文字列の先頭から指定した文字列をすべて除去するメソッド「lstrip([chars])」(left strip)
# chars はオプション：除去したい文字（複数指定可）
# デフォルトでは、**前後の空白文字（スペース・タブ・改行など）**を除去
exe_func("aaabbb/ccc/ddd/bbb","aaabbb/ccc/ddd/bbb".lstrip,"ab")

## 文字列の末尾から指定した文字列をすべて除去するメソッド「rstrip([chars])」(right strip)
# chars はオプション：除去したい文字（複数指定可）
# デフォルトでは、**前後の空白文字（スペース・タブ・改行など）**を除去
exe_func("aaabbb/ccc/ddd/aaabbb","aaabbb/ccc/ddd/aaabbb".rstrip,"ab")

# 長さが指定した値（widthの値）になるように左に0を詰めた文字列に変換するメソッド「zfill(width)」
# 文字列の長さが width より短い場合に、先頭にゼロを補う
exe_func("1223","1223".zfill,6)

# 文字列の先頭からprefixで指定した文字列を除去するメソッド「removeprefix(prefix, /)」
exe_func('aaa/bbb/ccc','aaa/bbb/ccc'.removeprefix,'aaa/')

# 文字列の末尾からsuffixで指定した文字列を除去するメソッド「removesuffix(siffix, /)」
exe_func('aaa/bbb/ccc', 'aaa/bbb/ccc'.removesuffix, '/ccc')