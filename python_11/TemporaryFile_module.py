import tempfile

# 'w+t'は読み書き可能なテキストモードを指定
with tempfile.TemporaryFile('w+t', encoding='utf-8') as fp:
    fp.write('Hello, world!\n')
    fp.write('This is a temporary file.')

    # ファイルの先頭に戻る
    fp.seek(0)
    
    # 内容を読み込む
    content = fp.read()
    print(content)
print('----------------------------------')
# 'with'ブロックを抜けると、fpは閉じられ、ファイルは自動的に削除されます。
# この時点でファイルにアクセスしようとするとエラーになります。

# NamedTemporaryFile
import tempfile

# 'delete=True' (デフォルト) でファイルを自動的に削除
with tempfile.NamedTemporaryFile(mode='w+t', delete=True) as fp:
    print(f"作成された一時ファイル名: {fp.name}")

    # ファイルに書き込み
    fp.write("これは名前付きの一時ファイルです。\n")
    fp.seek(0)  # ファイルポインタを先頭に戻す

    # ファイルから読み込み
    content = fp.read()
    print(f"ファイルの内容:\n{content}")

    # このファイルパスを他のプログラムに渡すことができます
    file_path = fp.name

print('----------------------------------')

# 'with'ブロックを抜けると、ファイルは自動的に削除されます。
# 以下の行は、ファイルが既に削除されているためエラーになります。
# print(os.path.exists(file_path))

# delete=false
import os

# 'delete=False' を指定すると、プログラム終了後もファイルが残る
fp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
try:
    print(f"作成された一時ファイル名: {fp.name}")
    fp.write("このファイルは手動で削除する必要があります。\n")

    # ファイルパスを保存
    file_path_to_keep = fp.name

    # ファイルを閉じる
    fp.close()

    # ファイルはまだ存在しています
    print(f"ファイルはまだ存在しますか？: {os.path.exists(file_path_to_keep)}")

finally:
    # 処理が終了したら、手動でファイルを削除
    os.remove(file_path_to_keep)
    print(f"ファイルは削除されましたか？: {not os.path.exists(file_path_to_keep)}")