import re
from shared import re_result

re_result(re.search, r'\w', 'あいうえおABC')
# ASCⅡのみにマッチ
re_result(re.search, r'\w', 'あいうえおABC', flags=re.A)

# I、IGNORECASE
    # 大文字小文字を区別せずマッチ

# 大文字小文字を区別するのでマッチしない
re_result(re.search,'[abc]+', 'ABC')
# 大文字小文字を無視するのでマッチ
re_result(re.search,'[abc]+', 'ABC', re.I)

# M、 MULTILINE
    # 複数行のテキストを指定したときに^と$が各行の先頭と末尾にマッチ
text = "abc\ndef\nghi"
pattern = "^def"
re_result(re.search,pattern, text, re.MULTILINE)

# S、 DOALL
# .が改行文字も含めてマッチ
re_result(re.search,'a.c', 'a\nc')
# .が各行文字にマッチ
re_result(re.search,'a.c', 'a\nc', re.S)