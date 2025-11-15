import re
from shared import re_result

# a.cの正規表現パターンを作成
pattern = re.compile('a.c')

# 正規表現オブジェクトのメソッドを実行
re_result(pattern.search,'abcde')

# reモジュールの関数を実行
re_result(re.search,'a.c', 'abcde')