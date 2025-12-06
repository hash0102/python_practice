from urllib import request,error

# url
# リダイレクトされる可能性のあるURL
url_redirect = 'http://httpbin.org/redirect-to?url=http://example.com'

with request.urlopen(url_redirect) as response:
    print(type(response))
    # `url`属性を使って最終的なURLを取得
    final_url = response.url
    print(f"最終的なURL: {final_url}")
    print(type(final_url))
    
    # `geturl()`メソッドでも同じ結果が得られる
    print(f"最終的なURL (geturl()): {response.geturl()}")
print('-'*30)

# headers
url = 'https://www.python.org'

with request.urlopen(url) as response:
    print(type(response))
    # `headers`属性でヘッダー全体を取得
    headers = response.headers
    print("Content-Typeヘッダー:", headers['Content-Type'])
    print("Dateヘッダー:", headers['Date'])
    print(type(headers))
    
    # `info()`メソッドでも同様に取得可能
    print("Content-Typeヘッダー (info()):", response.info()['Content-Type'])
print('-'*30)

# status

url_ok = 'https://www.python.org'
url_not_found = 'https://www.python.org/nonexistent_page'

# 正常なリクエスト
try:
    with request.urlopen(url_ok) as response:
        print(f"URL: {url_ok}")
        print(f"ステータスコード: {response.status}")
        print(f"ステータスコード (getcode()): {response.getcode()}")
except error.URLError as e:
    print(f"エラーが発生しました: {e.reason}")

print("-" * 30)

# エラーを返すリクエスト
try:
    with request.urlopen(url_not_found) as response:
        # このブロックは実行されない
        pass
except error.HTTPError as e:
    # 404エラーが発生した場合、`HTTPError`例外が捕捉される
    print(f"URL: {url_not_found}")
    print(f"HTTPエラーコード: {e.code}")
    print(f"エラー理由: {e.reason}")