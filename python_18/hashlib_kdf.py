import hashlib
import os

# 1. 鍵導出のパラメータを定義
password = b'my_super_secret_password'

# 16バイトのランダムなソルトを生成
salt = os.urandom(16)

# イテレーション回数。セキュリティを考慮して高めに設定
iterations = 100000 

# 2. pbkdf2_hmac()で鍵を導出
derived_key = hashlib.pbkdf2_hmac(
    'sha256',  # ハッシュアルゴリズム
    password,  # パスワード
    salt,      # ソルト
    iterations # イテレーション回数
)

# 導出された鍵のハッシュ値を表示
print("導出された鍵:", derived_key.hex())
print(type(derived_key.hex()))