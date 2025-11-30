import os

# 環境変数

# 環境変数を取得
print(os.environ['HOME'])         # 特定の環境変数を取得
print(os.environ.get('PATH'))    # 存在しないキーの場合はNoneを返す
print('----------------------------------')

# 環境変数を設定
os.environ['MY_VAR'] = 'hello'
print(os.environ['MY_VAR'])

# 環境変数を削除
del os.environ['MY_VAR']
print('----------------------------------')

# 環境変数の一覧
for key, value in os.environ.items():
    print(f"{key} = {value}")

# Windows OSではL22~L35の関数は使用できない（UNIX限定）
# ユーザーID・実効ユーザーID
# 現在のプロセスのユーザーID (UID)
"""
print(os.getuid())             # 実ユーザーID (real UID)
print(os.geteuid())            # 実効ユーザーID (effective UID)
 
# グループID・実効グループID
# グループID
print(os.getgid())              # 実グループID (real GID)
print(os.getegid())             # 実効グループID (effective GID)

# 所属グループID一覧
print(os.getgroups())           # 所属しているグループのIDリスト
"""
print('----------------------------------')
#  プロセスIDと親プロセスID

# プロセスID
print(os.getpid())              # 自分のプロセスID

# 親プロセスID
print(os.getppid())             # 親プロセスのID

print('----------------------------------')
# Windows OSではL51~L54の関数は使用できない（UNIX限定）
# スケジューリング優先度（プロセスのnice値）
""""
# 優先度（nice値）を取得
os.nice(0)               # 現在のnice値を取得（0を渡すとそのまま返る）

# 優先度を変更（+10すると優先度が下がる）
os.nice(10)              # プロセスのnice値を +10 増やす
"""