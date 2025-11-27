import sys
# sys.argv
print("引数のリスト:", sys.argv)
for i, arg in enumerate(sys.argv):
    print(f"argv[{i}] = {arg}")

# 例 $ python3 sys_module.py apple banana cherry
print('----------------------------------')

# sys.path
for path in sys.path:
    print(path)
print('----------------------------------')

# sys.exit

def divide(a, b):
    if b == 0:
        print("ゼロ除算エラー")
        sys.exit(1)
    return a / b

result = divide(10, 0)
print("結果:", result)  # 実行されない

# 引数チェックに使える
if len(sys.argv) != 2:
    print("使い方: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
print("処理対象ファイル:", filename)