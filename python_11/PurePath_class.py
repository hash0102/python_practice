from pathlib import PurePath

p = PurePath('folder', 'subfolder', 'file.txt')
print(F'型：{type(p)}')
print(p)               # folder/subfolder/file.txt（OSにより区切りが変わる）
print(p.name)          # file.txt
print(p.suffix)        # .txt
print(p.stem)          # file
print(p.parent)        # folder/subfolder
print(p.parts)         # ('folder', 'subfolder', 'file.txt')
print('----------------------------------')
# パスの結合
new_path = p.with_name('newfile.csv')
print(new_path)        # folder/subfolder/newfile.csv
print('----------------------------------')

# Windows風のパス（PurePathは自動でOSに合わせて解釈）
p2 = PurePath("C:/Users/example/file.tar.gz")

print("🔹 parts     :", p2.parts)
print("🔹 drive     :", p2.drive)
print("🔹 root      :", p2.root)
print("🔹 anchor    :", p2.anchor)
print("🔹 parents   :", list(p2.parents))
print("🔹 parent    :", p2.parent)
print("🔹 name      :", p2.name)
print("🔹 suffix    :", p2.suffix)
print("🔹 suffixes  :", p2.suffixes)
print("🔹 stem      :", p2.stem)

print('----------------------------------')

# PurePathのメソッド
# サンプルパスを定義
p3 = PurePath('/home/user/docs/report.txt')
r = PurePath('docs/report.txt')

# is_absolute：パスが絶対パスかどうか判定
print(p3.is_absolute())  # True
print(r.is_absolute())  # False
print('----------------------------------')

#  is_relative_to()（Python 3.9+）：指定したパスに対して相対パスかどうかをチェック
print(r.is_relative_to('docs'))       # True
print(r.is_relative_to('other'))      # False
print('----------------------------------')

# with_name(name)：名前の変更（拡張子含む）
# ディレクトリには使えない。最後の要素がファイル名である必要あり。
new_path = p3.with_name('summary.md')
print(new_path)  # /home/user/docs/summary.md
print('----------------------------------')

# with_stem(stem)：ファイル名のみ変更（拡張子保持）
# 拡張子はそのままなので、安全にファイル名だけ変えたいときに便利。
new_path = p3.with_stem('report_final')
print(new_path)  # /home/user/docs/report_final.txt
print('----------------------------------')

# with_suffix(suffix)：拡張子の変更・削除
print(p.with_suffix('.md'))   # /home/user/docs/report.md
print(p.with_suffix(''))      # /home/user/docs/report
print('----------------------------------')
