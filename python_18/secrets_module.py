import secrets
import string

# 許可する文字の集合
alphabet = string.ascii_letters + string.digits

# 32文字の安全なトークンを生成
token = ''.join(secrets.choice(alphabet) for i in range(32))

print(token)
print('文字数：', len(token))
print(type(token))

print('-' * 30)

# 32バイトのランダムなバイト列を生成
token2 = secrets.token_bytes(32)
print(token2)
print('バイト数：', len(token2))
print(type(token2))

print('-' * 30)

# 16バイトのバイト列を16進数文字列として生成 (長さは32文字)
token3 = secrets.token_hex(16)
print(token3)
print('文字数：', len(token3))
print(type(token3))

print('-' * 30)

# 16バイトのURLセーフなトークンを生成
token4 = secrets.token_urlsafe(16)
print(token4)
print('文字数：', len(token4))
print(type(token4))

print('-' * 30)

import hashlib

# パスワードを比較する関数
def verify_password(stored_hash, input_password):
    # 入力パスワードをハッシュ化
    input_hash = hashlib.sha256(input_password.encode('utf-8')).hexdigest()

    # ハッシュ値を安全に比較
    return secrets.compare_digest(stored_hash, input_hash)

# データベースに保存されたハッシュ値
stored_hash = hashlib.sha256(b'mysecretpassword').hexdigest()

# 正常な検証
print(verify_password(stored_hash, 'mysecretpassword'))

# 誤った検証
print(verify_password(stored_hash, 'wrongpassword'))