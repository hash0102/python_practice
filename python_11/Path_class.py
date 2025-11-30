from pathlib import Path

# 基本のパス定義
p = Path("example.txt")
print(type(p))
print(p)
print('----------------------------------')

# 基本情報取得
print("現在の作業ディレクトリ:", Path.cwd())
print("ホームディレクトリ:", Path.home())
print('----------------------------------')

# ファイルの属性チェック
print("ファイルが存在するか:", p.exists())
print("ディレクトリか:", p.is_dir())
print("ファイルか:", p.is_file())
print('----------------------------------')

# ファイルの情報とアクセス権
if p.exists():
    info = p.stat()
    print(f"サイズ: {info.st_size} bytes")
    print(f"最終更新: {info.st_mtime}")

    # chmod: アクセス権変更（UNIXのみ）
    # p.chmod(0o644)
print('----------------------------------')

# ディレクトリ操作
dir_path = Path("my_folder")

# ディレクトリ作成（存在しない場合）
dir_path.mkdir(exist_ok=True)

# ディレクトリの中身一覧
for f in dir_path.iterdir():
    print(f)
print('----------------------------------')

# パターンマッチ（ファイル検索）
for txt_file in dir_path.glob("*.txt"):
    print("txtファイル:", txt_file)
print('----------------------------------')

# ファイルの読み書き
# テキスト書き込み
p.write_text("Hello World")

# テキスト読み込み
print("読み込んだ内容:", p.read_text())
print('----------------------------------')

# その他の操作

dir_path2 = Path("exist_folder")
# ディレクトリ作成（存在しない場合）
dir_path2.mkdir(exist_ok=True)
print('ディレクトリ作成：',dir_path2)

file_path2 = dir_path2 / "example3.txt"
# ファイル作成
file_path2.touch()
print('ファイル作成：',file_path2)

# ファイル名変更
file_path2 = file_path2.rename(dir_path2 / "renamed.txt")
print('ファイル名変更：',file_path2)

# ディレクトリ名変更
dir_path2 = dir_path2.rename("delete_folder")
print('ディレクトリ名変更：',dir_path2)

# ファイルパスを更新（新しいディレクトリ名を反映）
file_path2 = dir_path2 / file_path2.name

# 絶対パスを取得
print("絶対パス:", file_path2.resolve())

# ファイル削除
print('ファイルが存在するか:',file_path2.exists())
if file_path2.exists():
    file_path2.unlink()

# 空ディレクトリ削除
if dir_path2.exists():
    dir_path2.rmdir()
print('----------------------------------')