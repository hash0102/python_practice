# stringモジュール
import string

# 英大文字 + 英小文字
print(F'string.ascii_lettersの実行結果：{string.ascii_letters}')
print('------------------------------------------------------')

# 英小文字（a〜z）
print(F'string.ascii_lowercaseの実行結果：{string.ascii_lowercase}') 
print('------------------------------------------------------')

# 英大文字（A〜Z）
print(F'string.ascii_uppercaseの実行結果：{string.ascii_uppercase}')
print('------------------------------------------------------')

# 数字（0〜9）
print(F'string.digitsの実行結果：{string.digits}')
print('------------------------------------------------------')

# 16進数（0〜9, a〜f, A〜F）
print(F'string.hexdigitsの実行結果：{string.hexdigits}')
print('------------------------------------------------------')

# 8進数（0〜7）
print(F'string.octdigitsの実行結果：{string.octdigits}')
print('------------------------------------------------------')

# 記号（!@#など）
print(F'string.punctuationの実行結果：{string.punctuation}')
print('------------------------------------------------------')

# 印刷可能文字（digits, letters, punctuation, whitespace）
print(F'string.printableの実行結果：{string.printable}')
print('------------------------------------------------------')

# 空白文字（space, \t, \n など）
print(F'string.whitespaceの実行結果：{string.whitespace}')      
print('------------------------------------------------------')

# 文字列が小文字かチェック
print(F'\'a\' in string.ascii_lowercaseの実行結果：{ 'a' in string.ascii_lowercase}')
print('------------------------------------------------------')