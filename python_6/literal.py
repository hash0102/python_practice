# シングルクォート
'hoge'
# ダブルクォート
"piyo"
# 三重引用符
'''huga'''
"""hugahuga"""

# \ を出力する「\\」
print('aaa\\')

# 'を出力する「\'」
print('aaa\'')

# "を出力する「\"」
print('aaa\"')

# 行送り（LF）を出力する「\n」
print('aaa\nbbb')

# ASCⅡ復帰（CR）を出力する「\r」
# CRとはカーソルを先頭に戻す指示のこと、そのため「ccc」が行頭に戻って、上書きされて出力される
print('aaa\rbbb\rccc')

# ASCⅡ水平タブ（TAB）を出力する「\t」
print('aaa\tbbb')

# 「r」でエスケープシーケンス無効
print(r'aaa\nbbb')

# 複数行
print((
    "hey Bob,"
    "Im Mark,"
    "Honestly, I'm Apple"
))