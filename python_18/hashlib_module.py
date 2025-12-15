import hashlib

# 1. SHA256アルゴリズムを選択
hasher = hashlib.sha256()

# 2. データを追加（バイト列にする必要がある）
hasher.update(b'hello, ')
hasher.update(b'world!')

# 3. ハッシュ値を取得
hash_value = hasher.hexdigest()
print(hash_value)
print(type(hash_value))

print('-' * 30)

# 1. 利用可能な全てのアルゴリズム名を確認
print(f"利用可能なアルゴリズム: {hashlib.algorithms_available}")
print(type(hashlib.algorithms_available))

# 2. アルゴリズム名が利用可能かチェック
algorithm_name = 'sha256'

if algorithm_name in hashlib.algorithms_available:
    # 3. hashlib.new()を使って動的にハッシュオブジェクトを生成
    hasher2 = hashlib.new(algorithm_name)
    hasher2.update(b'This is a test message.')
    print(f"{algorithm_name}のハッシュ値: {hasher2.hexdigest()}")
    print(type(hasher2.hexdigest()))
else:
    print(f"エラー: {algorithm_name} は利用できません。")

print('-' * 30)

# 4. 存在しないアルゴリズムを指定した場合
try:
    hashlib.new('invalid_algo')
except ValueError as e:
    print(f"エラーが発生しました: {e}")

print('-' * 30)

# update
hasher3 = hashlib.sha256()
hasher3.update(b'This is a ')
# 2回のupdateで、'This is a test message.'全体がハッシュ化される
hasher3.update(b'test message.')
print(hasher3)
print(type(hasher3))
print('-' * 30)

# digest
hasher4 = hashlib.sha256(b'hello')
hash_bytes = hasher4.digest()
print(hash_bytes)
print(type(hash_bytes))
print('-' * 30)

# hexdigest
hasher5 = hashlib.sha256(b'hello')
hash_string = hasher5.hexdigest()
print(hash_string)
print(type(hash_string))
print('-' * 30)