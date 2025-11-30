from pathlib import Path
path = Path('example4.txt')
# open
with open(path, 'w', encoding='utf-8') as f:
    f.write("Hello, Path-like world!")

# configpareser
import configparser

# ConfigParser オブジェクト
cfg = configparser.ConfigParser()

# DEFAULT セクションに設定を追加
cfg['DEFAULT'] = {
    'username': 'alice',
    'password': 'secret123'
}

# settings.ini に書き込む
with open('settings.ini', 'w') as f:
    cfg.write(f)

print(cfg.read('settings.ini'))

# DEFAULT セクションの値を取得
username = cfg['DEFAULT'].get('username', 'unknown')
password = cfg['DEFAULT'].get('password', 'none')

print("username:", username)
print("password:", password)
print('----------------------------------')

# zipfile
import zipfile

# ZIPに入れるファイルを準備する
Path("zip_samples").mkdir(exist_ok=True)

file1 = Path("zip_samples/file1.txt")
file2 = Path("zip_samples/file2.txt")

file1.write_text("これはファイル1です。")
file2.write_text("これはファイル2です。")

print("元ファイルを作成しました。")

# ZIPファイルを作成
with zipfile.ZipFile("data.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.write(file1, arcname="file1.txt")
    z.write(file2, arcname="file2.txt")

print("data.zip を作成しました。")

# ZIPを展開する
extract_dir = Path("extracted_files")
extract_dir.mkdir(exist_ok=True)

with zipfile.ZipFile("data.zip", "r") as z:
    z.extractall(extract_dir)

print("ZIPファイルを extracted_files フォルダに展開しました。")
print('----------------------------------')

# sqlite3
import sqlite3

# データベースに接続（無ければ作成される）
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# テーブル作成
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
""")

# データを追加
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
conn.commit()

# データを読み取る
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# 接続を閉じる
conn.close()
print('----------------------------------')

# shutil
import shutil

# コピー用のファイルとフォルダを準備する
# ファイル作成
file = Path("doc.txt")
file.write_text("これは doc.txt の内容です。")
print("doc.txt を作成しました。")

# フォルダ作成
project = Path("project")
project.mkdir(exist_ok=True)

# フォルダ内にファイルを作成
(project / "main.py").write_text("print('Hello from project!')")
(project / "readme.md").write_text("# Project README")

print("project フォルダを作成しました。")

# ファイルをコピー（shutil.copy）
shutil.copy("doc.txt", "doc_copy.txt")
print("doc.txt → doc_copy.txt にコピーしました。")

# フォルダをコピー（shutil.copytree）
shutil.copytree("project", "project_backup")
print("project → project_backup にコピーしました。")
print('----------------------------------')

# os
import os

# HOMEディレクトリを表示
print("Home directory:", os.environ.get('HOME'))

# temp.txt を作成する
temp_file = Path("temp.txt")
temp_file.write_text("これは一時ファイルです。")
print("temp.txt を作成しました。")


# temp.txt が存在するか確認
if os.path.exists("temp.txt"):
    print("temp.txt は存在します。 削除します。")
    
    # temp.txt を削除
    os.remove("temp.txt")
    print("temp.txt を削除しました。")
else:
    print("temp.txt は存在しません。")
print('----------------------------------')

# os.path
# チェックするファイルとフォルダ
files = ["doc.txt", "doc_copy.txt"]
folders = ["project", "project_backup"]

# ファイルの存在確認
for f in files:
    if os.path.exists(f):
        print(f"{f} は存在します。")
    else:
        print(f"{f} は存在しません。")

# フォルダの存在確認と中身リスト
for d in folders:
    dir_path = Path(d)
    if dir_path.exists() and dir_path.is_dir():
        print(f"{d} フォルダは存在します。")
        print("中身:", [p.name for p in dir_path.iterdir()])
    else:
        print(f"{d} フォルダは存在しません。")

# ファイルのフルパス取得（os.path.join と pathlib 両方）
for f in files:
    full_path = os.path.join(os.getcwd(), f)
    print(f"{f} のフルパス（os.path.join）:", full_path)

for f in files:
    full_path = Path(f).resolve()
    print(f"{f} のフルパス（Path.resolve）:", full_path)
