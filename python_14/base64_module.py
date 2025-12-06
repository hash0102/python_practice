import base64

# エンコードしたいバイナリデータ
data = b'Hello, World!'

# データをBase64でエンコード
encoded_data = base64.b64encode(data)

print(f"元のデータ: {data}")
print('元の型：', type(data))
print('-' * 30)
print(f"エンコードされたデータ: {encoded_data}")
print('エンコードされた型：', type(encoded_data))
# `==`は、元のデータがBase64の3バイトのブロックに満たない場合にパディングとして追加される
print('-' * 30)
# Base64文字列をデコードして元に戻す
decoded_data = base64.b64decode(encoded_data)
print(f"デコードされたデータ: {decoded_data}")
print(f"デコードされた型: {type(decoded_data)}")
print('-' * 30)

# utf-8でエンコードした値を渡す
string_data = "日本語"
bytes_data = string_data.encode('utf-8')

# Base64でエンコード
encoded_data2 = base64.b64encode(bytes_data)

print(f"元の文字列: {string_data}")
print(f"バイト列: {bytes_data}")
print(f"エンコードされたデータ: {encoded_data2}")
print('-' * 30)

# Base64でエンコードされたバイト文字列
encoded_data3 = b'SGVsbG8sIFdvcmxkIQ=='

# データをデコード
decoded_data2 = base64.b64decode(encoded_data3)

print(f"エンコードされたデータ: {encoded_data3}")

print(f"デコードされたデータ: {decoded_data2}")

# さらに、デコードされたバイト文字列をテキストとして扱う場合は、デコードが必要
original_string = decoded_data.decode('utf-8')
print(f"元の文字列: {original_string}")

print('-' * 30)

# 日本語の文字列をBase64でエンコードしたもの
encoded_japanese = b'5pel5pys6aSo'

# デコード
decoded_bytes = base64.b64decode(encoded_japanese)

# バイト文字列をUTF-8でデコードして元の日本語文字列に戻す
original_japanese = decoded_bytes.decode('utf-8')

print(f"エンコードされたデータ: {encoded_japanese}")

print(f"デコードされた日本語: {original_japanese}")