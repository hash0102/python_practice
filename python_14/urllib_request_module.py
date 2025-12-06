from  urllib import request, error, parse

# urlopen()

# GETリクエスト

url = "https://www.example.com"

try:
    # urlopenでリクエスト
    with request.urlopen(url) as response:
        # レスポンスをバイト列で取得
        data = response.read()
        
        # UTF-8でデコード
        html = data.decode('utf-8')
        
        # ステータスコードとHTMLの先頭表示
        print(f"ステータスコード: {response.getcode()}")
        print("HTMLの先頭部分:")
        print(html[:500])

except error.URLError as e:
    print(f"エラーが発生しました: {e.reason}")
print('-'*30)

# POSTリクエスト

url2 = 'https://httpbin.org/post'
data2 = {'name': 'Tanaka', 'age': 30}

# データをURLエンコードし、bytes形式に変換
encoded_data = parse.urlencode(data2).encode('utf-8')

try:
    # data引数を指定すると、urlopen()は自動的にPOSTリクエストとして扱う。
    with request.urlopen(url2, data=encoded_data) as response:
        # レスポンスはJSON形式で返される
        response_data = response.read().decode('utf-8')
        print(f"ステータスコード: {response.getcode()}")
        print("レスポンスデータ:")
        print(response_data)
except error.URLError as e:
    print(f"エラーが発生しました: {e.reason}")
print('-'*30)

# DELETEメソッドのリクエスト例

# 削除対象のリソースを示すURL
url = 'https://httpbin.org/delete'

# Requestオブジェクトを作成
# method='DELETE'を指定して、DELETEリクエストであることを明示
request2 = request.Request(url, method='DELETE')

print(f"URL: {request2.full_url}")
print(f"HTTPメソッド: {request2.get_method()}")

try:
    with request.urlopen(request2) as response:
        # レスポンスを取得してデコード
        response_body = response.read().decode('utf-8')
        status_code = response.getcode()
        
        print("\n--- レスポンス ---")
        print(f"ステータスコード: {status_code}")
        print("ボディ:")
        print(response_body)

except error.HTTPError as e:
    print(f"HTTPエラーが発生しました: {e.code} - {e.reason}")
except error.URLError as e:
    print(f"URLエラーが発生しました: {e.reason}")
print('-'*30)