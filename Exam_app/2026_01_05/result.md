### 次の正規表現に関するコードで、結果が「`'03'`」にならないものはどれか。

```python
# reモジュールをインポートしているものとする。

選択 1
obj = re.match(r'(\d+)-(\d+)-(\d+)', '03-1234-5678')
obj.group(1)

選択 2
obj = re.match('(\\d+)-(\\d+)-(\\d+)', '03-1234-5678')
obj.group(1)

選択 3
obj = re.match(r'(\d+)-(\d+)-(\d+)', '03-1234-5678')
obj.group(0)[1]

選択 4
obj = re.match(r'(\d+)-(\d+)-(\d+)', '03-1234-5678')
obj[1]
```

**A.**
```python
obj = re.match(r'(\d+)-(\d+)-(\d+)', '03-1234-5678')
obj.group(0)[1]
```

- 選択肢3が正解
- 選択肢の記述にある「`obj`」は、**マッチオブジェクトを代入した変数**
- マッチオブジェクトとは、**正規表現にマッチした文字列の情報を格納し**たオブジェクト

- 正規表現を「`()`」で囲むとサブグループが生成され、グループとして取り出すことができる
- 「`()`」で囲んだマッチオブジェクトに対して、`group()`メソッドやインデックスで要素を指定すると、特定のグループの文字列を取得できる
<br>

**【選択肢1】**
```python
obj = re.match(r'(\d+)-(\d+)-(\d+)', '03-1234-5678')
obj.group(1)
```

- **グループの指定はインデックスと違って1から開始**
- ここでは1番目のグループを指定しているため、結果は「`'03'`」になる
- `obj.group(2)`であれば「`'1234'`」、`obj.group(3)`であれば「`'5678'`」になる
- `obj.group(0)`と指定すると、**マッチした文字列全体を取得**するため、結果は「`'03-1234-5678'`」になる

**【選択肢2】**
```python
obj = re.match('(\\d+)-(\\d+)-(\\d+)', '03-1234-5678')
obj.group(1)
```

- 選択肢1と違ってバックスラッシュが2つあり、raw文字列の「`r`」がありませんが、**結果は選択肢1と同じ**
- Pythonの正規表現で**バックスラッシュを使う場合は、raw文字列を使うことが推奨**されています。
- 例えば正規表現で数字を表す「`\d`」は、それが正規表現の特殊文字であることを明確にするために、本来は「`\\d`」と記述するべきですが、実際は「`\d`」でも機能する
- 機能しますが不明確なため、raw文字列を使って特殊文字であることを明確にすることが推奨されている

**【選択肢3】**
```python
obj = re.match(r'(\d+)-(\d+)-(\d+)', '03-1234-5678')
obj.group(0)[1]
```
- `group(0)`の「0」は**マッチした文字列全体を取得**するため、「`obj.group(0)`」の結果は「`'03-1234-5678'`」になる

- 「`obj.group(0)[1]`」は、文字列の「`'03-1234-5678'`」に対してインデックス「`[1]`」を指定しているため、結果は「`'03'`」ではなく「`'3'`」となる


**【選択肢4】**
```python
obj = re.match(r'(\d+)-(\d+)-(\d+)', '03-1234-5678')
obj[1]
```
- 正規表現のマッチオブジェクトは、**`group()`メソッドだけではなくインデックス指定でも取得できる**
- 文字列やリストをインデックスで取得する場合は0から開始しますが、**マッチオブジェクトのグループをインデックスで取得する場合は、0ではなく1から開始**
- そのため**「`obj[1]`」は「`obj.group(1)`」と同じ処理**になり、選択肢1、2と同じ結果になる
- なお、「`obj[0]`」とした場合は「`'03-1234-5678'`」が返る

### jsonモジュールのdumps()関数で、datetimeのようにシリアライズできないオブジェクトをstr型に変換する場合、次のコードの【A】【B】に記述するものはどれか。

```python
from datetime import datetime
import json

book = {"name": "Python", "pub": datetime(2000, 12, 1)}

def func(obj):
    if 【A】(obj, datetime):
        return obj.isoformat()

print(json.dumps(book, 【B】=func))
```

```python
選択 1
【A】 type
【B】 default

選択 2
【A】 type
【B】 defaultdict

選択 3
【A】 isinstance
【B】 default

選択 4
【A】 isinstance
【B】 defaultdict
```

A. 
```python
【A】 isinstance
【B】 default
```
- 選択肢3が正解です。
- jsonモジュールの`dumps()`関数は、引数「`default`」で**関数を指定**することで、**シリアライズ（JSON形式への変換）できないデータ型を、シリアライズできるデータ型に変換**します。

- 例えば、Pythonのdatetime型はシリアライズできません。

- そのため問題文では、`isinstance()`関数でオブジェクトが`datetime`型か判定し、`datetime`型だった場合は`isoformat()`関数で文字列に変換しています。


- 問題文の結果は、文字列の「`{"name": "Python", "pub": "2000-12-01T00:00:00"}`」になります。

- 一見すると辞書のようですが、`type()`関数で判定すると「`str`」となります。

- `dumps()`関数は、JSONのルールに合わせて文字列に変換しているだけであり、変換後のPythonでのデータ型はstrです。


- なお、選択肢2と4の`defaultdict`はデフォルト値を持った辞書を作るクラスです。

- また、選択肢1と2の`type()`関数は引数を2つ指定することはできません。

### クエリ文字の「`'id=a%20c'`」を得たい場合、【A】と【B】に記述するものはどれか。

```python
from urllib import parse

parse.【A】({'id': 'a c'}, quote_via=parse.【B】)
```

```python
選択 1
【A】 urlencode
【B】 quote

選択 2
【A】 urlparse
【B】 parse_qs

選択 3
【A】 parse_qs
【B】 urlencode

選択 4
【A】 quote
【B】 urlparse
```


**A.**
``` python
【A】 urlencode
【B】 quote
```
- 選択肢1が正解です。
- parseモジュールの関数は名前がまぎらわしいですが、まとめると以下になります。

**`urlparse()`**
- URLをパース（解析）して結果を返します。
  - **`scheme`などの属性名や、インデックスで値を取得**します。


**`parse_qs()`**
- クエリ文字をパースして**辞書で返します**。
- `urlparse()`で**取得した属性「`query`」を引数**にすることができます。

**`urlencode()`**
- **辞書からクエリ文字**を組み立てます。

**`quote()、quote_plus()`**
- 文字列を**パーセントエンコード**してURLとして使えるようにします。
- `quote()`は空白を「`%20`」に変換し、`quote_plus()`は空白を`「+`」に変換します。
- `quote()`と`quote_plus()`は、parseモジュールのメソッドで使用して**URL全体を変換**することもできますが、問題文のように`urlencode()`の引数「`quote_via`」に指定してクエリ文字の変換でも使用できます。
- `urlencode()`はデフォルトで`quote_plus`が適用され、空白が「`+`」に変換されます。
- 問題文のように **`quote`を指定すると、空白が「`%20`」に変換**されます。

### 次のコードをインタープリタで順番に実行する場合、【A】と【B】に記述するものはどれか。
```bash
>>> import os

>>> from unittest.mock import 【A】

>>> os.path.join('dir', 'file.txt')

'dir/file.txt' # 結果

>>> 【B】 【A】('os.path.join', return_value='dummy'):
...   os.path.join('dir', 'file.txt')

'dummy' # 結果

>>> os.path.join('dir', 'file.txt')

'dir/file.txt' # 結果
```

```python
選択 1
【A】 MagicMock
【B】 mock

選択 2
【A】 patch
【B】 mock

選択 3
【A】 MagicMock
【B】 with

選択 4
【A】 patch
【B】 with
```

**A.**
```python
【A】 patch
【B】 with
```

- 選択肢4が正解です。
- **特定のクラスやメソッドをモックオブジェクトで置き換える**場合は、`unittest.mock`の`patch()`関数を使います。

- `patch()`関数は**デコレーター**を利用する方法と**コンテキストマネージャー**を利用する方法があり、問題文はコンテキストマネージャーを利用しています。

- コンテキストマネージャーを利用する場合は`with`文を使うため、【A】に`patch`が入り、【B】に`with`が入ります。

```python
import os
from unittest.mock import patch

os.path.join('dir', 'file.txt')

# os.path.join()関数でパスを結合しているため、結果が「'dir/file.txt'」になります。


with patch('os.path.join', return_value='dummy'):
  os.path.join('dir', 'file.txt')

# patch()関数で、os.path.join()関数の戻り値が「'dummy'」になるように変更しているため、結果が「'dummy'」になります。


os.path.join('dir', 'file.txt')

# with文を抜けて、os.path.join()関数の処理が元に戻るため、結果が「'dir/file.txt'」になります。

```

### URL用のトークンを比較する場合、次のコードの【A】と【B】に記述するものはどれか。

```python
import secrets
from urllib import parse

token = secrets.【A】

url = 'https://sample.com/?id=' + token

url_parse = parse.urlparse(url)

qs =  parse.parse_qs(url_parse.query)

secrets.【B】(token, qs['id'][0])
```

```python
選択 1
【A】 token_urlsafe()
【B】 compare_digest

選択 2
【A】 token()
【B】 compare_digest

選択 3
【A】 token_urlsafe()
【B】 compare

選択 4
【A】 token()
【B】 compare
```

**A.**
```python
【A】 token_urlsafe()
【B】 compare_digest
```

- 選択肢1が正解です。

- `secrets`モジュールで`Base64`のURL用トークンを作成する場合は、`token_urlsafe()`メソッドを使います。
- また、送信したトークンと受信したトークンを比較する場合は、タイミング攻撃のセキュリティリスクを避けるために、`==`ではなく`compare_digest()`メソッドを使います。
- 問題文の処理の流れは以下となります。

```python
token = secrets.token_urlsafe()

# token_urlsafe()でトークンを生成。

# tokenの例: '8wj6n5NHSUc7zvrpZFrkaBChnwpQqpGr_egFHfX6PPs'

url = 'https://sample.com/?id=' + token

# URLの文字列にトークンを結合。

url_parse = parse.urlparse(url)

# urlparse()で、URLを「scheme（https）」や「query（?id=' + token）」に分解。

qs =  parse.parse_qs(url_parse.query)

# parse_qs()で、「query（?id=' + token）」を、辞書「{'id': [token]}」に変換。

# qs = {'id': ['8wj6n...']} 
# parse_qs()で生成される辞書の値がリストであることに注意。

secrets.compare_digest(token, qs['id'][0])

# compare_digest()で、最初に生成したトークン（token）と、URLから抽出したトークン（qs['id'][0]）を比較し、「True」が返る。

# qs['id'] = ['8wj6n...']
#  「qs['id']」はリストで、「token」は文字列のため、比較するとエラーになる。

# qs['id'][0] = '8wj6n...'
# 「qs['id'][0]」はリストの0番目の要素を取得しているため、文字列の「'8wj6n...'」が返り、「token」と比較可能になる。
```

- 実際の運用では、サーバで生成したトークンと、クライアントから受信したトークンを比較し、正しいトークンであることを検証します。