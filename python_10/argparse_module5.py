import argparse

# 1. ArgumentParser インスタンス作成
parser = argparse.ArgumentParser(description="名前とスコアを受け取るスクリプト")

# 2. オプション定義
parser.add_argument("-n", "--name", help="ユーザーの名前", required=True)
parser.add_argument("-s", "--score", help="スコア（整数）", type=int, required=True)

# 3. 引数をパース
args = parser.parse_args()

# 4. 変数に格納
name = args.name
score = args.score

# 5. 値を扱う
print(f"こんにちは、{name}さん！")
print(f"あなたのスコアは {score} 点です。")

# $ python3 ./argparse_module5.py -n Alice -s 92で実行