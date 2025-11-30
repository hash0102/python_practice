import shutil
import os

# ディレクトリとファイルを作成
os.makedirs('my_dir/sub_dir', exist_ok=True)
with open('my_dir/sub_dir/file.txt', 'w') as f:
    f.write('Hello')

# my_dir ディレクトリツリー全体を削除
shutil.rmtree('my_dir')

# ディレクトリとファイルを作成
os.makedirs('old_dir', exist_ok=True)
with open('old_dir/my_file.txt', 'w') as f:
    f.write('Move me!')

# old_dirをnew_dirに移動
shutil.move('old_dir', 'new_dir')

# ソースディレクトリを作成
os.makedirs('source_dir/sub_dir', exist_ok=True)
with open('source_dir/sub_dir/data.txt', 'w') as f:
    f.write('Copy me!')

# source_dirをdestination_dirにコピー
shutil.copytree('source_dir', 'destination_dir')