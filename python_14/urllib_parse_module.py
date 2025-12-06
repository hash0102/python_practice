import urllib.parse

url = 'https://www.example.com:8080/path/to/resource?query=value#fragment'

# urlparse
parsed_url = urllib.parse.urlparse(url)

print(parsed_url)
print(type(parsed_url))
print('-'*30)

# `ParseResult`の属性にアクセスする例
print(f"スキーム: {parsed_url.scheme}")
print(f"ネットロケーション: {parsed_url[1]}")
print(f"パス: {parsed_url[2]}")
print(f"クエリ: {parsed_url.query}")
print(f"フラグメント: {parsed_url.fragment}")
print('-'*30)

query_string = 'name=John+Doe&age=30'
# parse_qs
parsed_query = urllib.parse.parse_qs(query_string)

print(parsed_query)
print(type(parsed_query))

# 値へのアクセス
print(parsed_query['name'][0])
print(type(parsed_query['name'][0]))
print('-'*30)

# keep_blank_values=Trueを使うと、空の値も取得できる

# stateには何も指定しない
query_string2 = 'name=John&name=Jane&city=New+York&state='

# デフォルト（keep_blank_values=False）
parsed_default2 = urllib.parse.parse_qs(query_string2)
print(parsed_default2)
print(type(parsed_default2))

# keep_blank_values=True
parsed_with_blank = urllib.parse.parse_qs(query_string2, keep_blank_values=True)
print(parsed_with_blank)
print(type(parsed_with_blank))
print('-'*30)

# parse_qs()とurlparse()の連携
url2 = 'https://www.example.com/search?query=python&lang=ja'

# urlparse()でクエリ文字列を抽出
parsed_url2 = urllib.parse.urlparse(url)
print(f"抽出されたクエリ文字列: {parsed_url2.query}")

# parse_qs()でクエリ文字列を解析
parsed_query3 = urllib.parse.parse_qs(parsed_url2.query)
print(f"解析結果: {parsed_query3}")
print('-'*30)

data = {
    'name': '田中 太郎',
    'age': 30,
    'city': '東京'
}

# urlencode
encoded_data = urllib.parse.urlencode(data)
'''
 日本語の文字列（UTF-8）がパーセントエンコーディングに変換され、
スペースが+に変換されている
'''
print(encoded_data)
print(type(encoded_data))
print('-'*30)

# 同じキーを持つデータをエンコードする場合、doseq=Trueが役立つ

data2 = {
    'item': ['apple', 'banana'],
    'city': 'New York'
}

# doseq=False（デフォルト）の場合
encoded_default = urllib.parse.urlencode(data2)
print(f"doseq=False: {encoded_default}")
# リストを 文字列としてそのままエンコード してしまう。

# doseq=Trueの場合
encoded_doseq = urllib.parse.urlencode(data2, doseq=True)
print(f"doseq=True: {encoded_doseq}")
# リストの要素を 展開して複数のキーとしてエンコード してくれる。
print('-'*30)

# quote()

# スペースを含む文字列のエンコード
path_string = 'my folder/file name.txt'
encoded_path = urllib.parse.quote(path_string)
print(f"quote()によるパスのエンコード: {encoded_path}")
# スペースが'%20'に、スラッシュはそのまま

# 日本語を含む文字列のエンコード
japanese_string = '日本語のファイル.txt'
encoded_japanese = urllib.parse.quote(japanese_string)
print(f"quote()による日本語のエンコード: {encoded_japanese}")
print('-'*30)

# quote_plus()

# スペースを含む文字列のエンコード
query_value = 'Python プログラミング'
encoded_query = urllib.parse.quote_plus(query_value)
print(f"quote_plus()によるクエリの値のエンコード: {encoded_query}")
# スペースが'+'に、日本語はパーセントエンコーディングに変換

# 予約文字を含む文字列のエンコード
reserved_chars = 'search&q=python'
encoded_reserved = urllib.parse.quote_plus(reserved_chars)
print(f"quote_plus()による予約文字のエンコード: {encoded_reserved}")
#'&'と'='がパーセントエンコーディングに変換
print('-'*30)

# safe引数
# パス部分のスラッシュをエンコードしたい場合
path_with_slash = 'path/to/resource'
encoded_path = urllib.parse.quote(path_with_slash, safe='') # safeに空文字列を指定
print(f"safe=''によるエンコード: {encoded_path}")
print('-'*30)

# urljoin()
base_url = 'https://www.example.com/path/to/page.html'

# 相対パスを結合
# ベースURLのpage.htmlが相対パスのanother_page.htmlで上書きされる。
new_url = urllib.parse.urljoin(base_url, 'another_page.html')
print(new_url)

# 階層をさかのぼる場合(相対パスを1階層上げる)
new_url_up = urllib.parse.urljoin(base_url, '../images/logo.png')
print(new_url_up)
print('-'*30)

# 絶対パスを結合
base_url2 = 'https://www.example.com/folder/page.html'

# 相対URLが絶対パス(/)で始まる場合、ベースURLのパス部分(folder/page.html)は無視される。
new_url_abs = urllib.parse.urljoin(base_url2, '/static/style.css')
print(new_url_abs)
print('-'*30)

# 完全なURLを結合する
base_url3 = 'https://www.example.com/path/to/page.html'

# 相対URLが完全なURL（スキームとネットロケーションを含む）の場合、ベースURLは無視される
full_url = urllib.parse.urljoin(base_url3, 'https://sub.example.com/new_page.html')
print(full_url)