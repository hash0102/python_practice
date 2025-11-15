from shared import exe_func

# 文字列中にsubが出現する位置を返し、存在しない場合は「-1」を返すメソッド「string.find(sub[, start[, end]])」
text = "banana"
# → 3（2文字目以降で 'a' を探す）
exe_func(text,text.find,"a",2)
# → 5（インデックス4〜5で 'a' を探す）
exe_func(text,text.find,"a", 4, 6)

text = "hello world"
# → 6
exe_func(text,text.find, "world")   
# → 4（最初の 'o' の位置）
exe_func(text,text.find, "o")
# → -1（見つからない）
exe_func(text,text.find, "x")

# 引数として指定した複数の文字列を結合するメソッド「'区切り文字'.join(文字列のリストやタプル)」
words = ['apple', 'banana', 'cherry']
print(F"\",\".join({words})の実行結果：{",".join(words)}")
print('------------------------------------------------------')

# 文字列が指定した接頭文字列で始まるかを判定するメソッド「startswith(prefix[, start[, end]])」
text = "Python programming"
# → True
exe_func(text,text.startswith,"Python")
# → False（大文字小文字は区別される）
exe_func(text,text.startswith,"python")

text = "Hello world"
# → True（6文字目以降が 'world'）
exe_func(text,text.startswith,"world",6)

# 文字列が特定の接尾文字列（末尾）で終わるかを判定するメソッド「endswith(suffix[, start[, end]])」
filename = "report.pdf"
# → True
exe_func(filename,filename.endswith,".pdf")
# → False
exe_func(filename,filename.endswith,".txt")

text = "HelloWorld"
# → True （text[3:5] は "lo"）
exe_func(text,text.endswith,"lo", 3, 5)

#  文字列（str）を バイト列（bytes）に変換するメソッド「encode(encoding='utf-8', errors='strict')」
# encoding：使いたい文字エンコーディング（例：utf-8, shift_jis, ascii など）
# errors（省略可）：エンコードエラー時の対処方法
    # 'strict'（デフォルト） → エラーを発生させる
    # 'ignore' → エラーを無視
    # 'replace' → 代替文字で置き換える（通常は ?）

text = "こんにちは"
exe_func(text, text.encode,'utf-8')