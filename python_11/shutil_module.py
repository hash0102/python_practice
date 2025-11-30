import shutil
import os
import stat
import time
from pathlib import Path 

# 読み取り専用にパーミッション変更
os.chmod("example.txt", 0o400)  # -r--------

# ファイルコピー
try:
    # コピー（内容のみ）
    shutil.copyfile("example.txt", "example_copy.txt")
except Exception as e:
    print("copyfile エラー:", e)

try:
    # コピー（内容 + パーミッション）
    shutil.copy("example.txt", "example_copy2.txt")
except Exception as e:
    print("copy エラー:", e)

try:
    # コピー（内容 + パーミッション + メタデータ）
    shutil.copy2("example.txt", "example_copy3.txt")
except Exception as e:
    print("copy2 エラー:", e)

# copymode(): パーミッションだけコピー
try:
    shutil.copyfile("example.txt", "example_copymode.txt")
    shutil.copymode("example.txt", "example_copymode.txt")
except Exception as e:
    print("copymode エラー:", e)

# copystat(): パーミッション + メタデータコピー
try:
    shutil.copyfile("example.txt", "example_copystat.txt")
    shutil.copystat("example.txt", "example_copystat.txt")
except Exception as e:
    print("copystat エラー:", e)

print("ファイルコピー完了（copymode/copystat 含む）")

# パーミッションとメタデータを確認する関数
def print_file_info(file_path):
    try:
        st = os.stat(file_path)
        mode = stat.filemode(st.st_mode)  # パーミッション
        size = st.st_size                  # サイズ
        mtime = time.ctime(st.st_mtime)    # 最終更新時刻
        print(f"{file_path}:")
        print(f"  パーミッション: {mode}")
        print(f"  サイズ: {size} バイト")
        print(f"  最終更新: {mtime}")
        print("-" * 40)
    except Exception as e:
        print(f"{file_path} 情報取得エラー:", e)

# 各ファイルの情報を表示
all_files = [
    "example.txt",
    "example_copy.txt",
    "example_copy2.txt",
    "example_copy3.txt",
    "example_copymode.txt",
    "example_copystat.txt"
]

for f in all_files:
    print_file_info(f)

# コピーしたファイルを削除（読み取り専用の場合は書き込み可能にしてから削除）
for f in all_files[1:]:  # 元ファイル example.txt は残す
    file_path = Path(f)
    if file_path.exists():
        try:
            # 削除前に書き込み可能に変更
            os.chmod(file_path, 0o600)  # -rw-------
            os.remove(file_path)
            print(f"{f} を削除しました。")
        except Exception as e:
            print(f"{f} 削除エラー:", e)
