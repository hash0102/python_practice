import tempfile
import os

# 'with'文でTemporaryDirectoryを使用
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"作成された一時ディレクトリのパス: {tmpdir}")
    
    # 一時ディレクトリ内にファイルを作成
    filepath = os.path.join(tmpdir, "my_temp_file.txt")
    with open(filepath, "w") as f:
        f.write("これは一時ファイルです。")
    
    # ファイルが一時ディレクトリ内に存在することを確認
    print(f"ファイルは存在しますか？ {os.path.exists(filepath)}")

# 'with'ブロックを抜けると、tmpdirとmy_temp_file.txtは自動的に削除されます。
# 以下の行はエラーになります（またはFalseを返します）
print(f"ディレクトリはまだ存在しますか？ {os.path.exists(tmpdir)}")
print('----------------------------------')

# with文なし
tmp_dir_obj = tempfile.TemporaryDirectory()
tmp_dir_path = tmp_dir_obj.name

# ...処理...

# 手動でクリーンアップ
tmp_dir_obj.cleanup() 