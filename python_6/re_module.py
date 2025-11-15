import re
from shared import re_result

# マッチする場合はオブジェクトを返す
re_result(re.search,'a.c', 'abcde')

re_result(re.match,'a.c', 'abcde')

# searchは文字列の途中でもマッチする
re_result(re.search,'.c', 'abcde')

# matchは先頭からのため、マッチせずNoneを返す
re_result(re.match,'.c', 'abcde')