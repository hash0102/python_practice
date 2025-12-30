### 次のコードで文字列の先頭が "Hello" か確認する正しい方法はどれか？


```python
import re

s = "Hello world"
```

```python
1. re.search(r"^world", s)
2. re.match(r"world", s)
3. re.match(r"Hello", s)
4. re.findall(r"Hello$", s)
```

**回答**

`re.findall(r"Hello$", s)`

**正解**
`re.match(r"Hello", s)`

**解説**
- `re.match`は**文字列の先頭でマッチ**する。
- `re.search`は**文字列全体で検索するため先頭限定ではない。**
- ここでの `r` は 「**生文字列（raw string）**」 を意味します。
- `r` を付けると バックスラッシュ `\` を**特殊文字として扱わず、そのまま文字として解釈**する。

例
```python
s1 = "Hello\nWorld"   
# \n は改行として解釈される

s2 = r"Hello\nWorld"  
# \n は文字列としてそのまま \ と n に
```

### 次のコードで文字 `'é' `を正規化してアクセントを分解した形にする正しい方法はどれか？

```python
1. unicodedata.decompose(s)
2. unicodedata.strip(s)
3. unicodedata.normalize("NFC", s)
4. unicodedata.normalize("NFD", s)
```

**回答**
`unicodedata.normalize("NFC", s)`

**正解**
`unicodedata.normalize("NFD", s)`

**解説**
- この問題の目的は、文字` 'é' `を アクセントを分解した形（`e` と `´` に分ける）に**正規化する方法**を問うものです。
- ※正規化（Normalization）とは、**文字列を 統一的な形に変換する操作**のことです。

**Unicode 正規化の種類(`unicodedata.normalize(form, s)` )**

- **NFC 正規合成（Composite）**　　 
  - `'é'`：**1文字（U+00E9）**
- **NFD 正規分解（Decomposed）**
  - `'é'`：`'e'` + `´`（U+0065 + U+0301）
- **NFKC 互換合成**             　　　　　
  - 互換文字も合成
- **NFKD 互換分解**
  - 互換文字も分解

### time モジュールで 14:30:15 を表すオブジェクトを作る正しい方法は？

```python
1. t = time(14,30,15)
2. t = datetime.time(14:30:15)
3. t = datetime.time(14,30,15)
4. t = time.time(14,30,15)
```

**回答**
`t = time.time(14,30,15)`

**正解**
`t = datetime.time(14,30,15)`

**解説**
- `time`クラスは **`datetime`モジュール内に存在**する
- `datetime.time(hour, minute, second)` で作成可能
- Python標準の **time モジュールには直接コンストラクタはない**

**`time `モジュール**
- 主にタイムスタンプや経過時間の取得・変換に使う
- `time()` は**現在時刻の秒数（UNIXタイム）を返す**

**`datetime`モジュール**
- 日付や時刻のオブジェクトを作成できる
- `datetime.time(hour, minute, second)` で時刻オブジェクトを作れる

### `nums = [1,3,5,7]`に`4`を挿入するコードは？

```python
1. bisect.bisect(nums, 4)
2. nums.insert(4)
3. nums.append(4)
4. bisect.insort(nums, 4)
```

**回答**
`nums.append(4)`

**正解**
`bisect.insort(nums, 4)`

**解説**
- この問題はソート済みリストに値を正しい位置で挿入する方法を問うものです。
- `bisect` **モジュールは ソート済みリストの探索や挿入を簡単に行うための標準モジュール**です。



**`bisect.bisect(list, x)`**
- 挿入すべき位置を返す

**`bisect.insort(list, x)`**
- ソート順を保ったままリストに挿入する

### 次のコードで、Bird クラスが Animal クラスを正しく継承しているものはどれ？

```python
class Animal:

    def speak(self):
        return "Some sound"
```

1. 
```python
class Bird extends Animal:
    pass
```

2. 
```python
class Bird(Animal):

    def speak(self):
        return "Tweet"
```


3. 
```python
class Bird(Animal):
    pass
```

4. 
```python
class Bird():
    pass
```

**回答**
```python
class Bird(Animal):
    pass
```

**正解**
```python
class Bird(Animal):

    def speak(self):
        return "Tweet"
```

**解説**
**Python の継承の正しい書き方**
```python
class 子クラス(親クラス):

    ...
```

### `urllib.request.urlopen()`で取得したデータをテキストとして表示する正しい方法はどれか？

```python
1. res.text
2. res.read().decode("utf-8")
3. res.decode()
4. res.read().text()
```

**回答**
`res.decode()`

**正解**
`res.read().decode("utf-8")`

**解説** 
- `urllib.request`は、Python標準ライブラリに含まれている HTTP通信を行うためのモジュール です。

- `urllib.request.urlopen()` は、**HTTPレスポンスオブジェクト（http.client.HTTPResponse）を返します。**

- このオブジェクトからデータを取得するには、まず **`read()`メソッドでバイト列 (bytes)を読み込みます。**

```python
import urllib.request

res = urllib.request.urlopen("https://example.com/")
data = res.read()
```

- `data` はバイナリデータ(機械語)なので、そのままでは文字列として扱えません。
- UTF-8 などの文字コードでデコードして文字列 (str) に変換する必要があります。

```python
text = data.decode("utf-8")
print(text)
```

- 読み込みとデコードをまとめた処理が、`text = res.read().decode("utf-8")`

※`read()`メソッドは引数がない場合、デフォルト動作ですべてのデータを最後まで読み込む


### 次のコードで Unicode 文字のカテゴリを取得する正しい関数はどれか？

```python
import unicodedata

c = "A"
```

```python
1. unicodedata.category(c)
2. unicodedata.name(c)
3. unicodedata.codepoint(c)
4. unicodedata.type(c)
```

**回答**
`unicodedata.codepoint(c)`

**正解**
`unicodedata.category(c)`

**解説**
- `category()`
  - "Lu"など**Unicodeカテゴリを返す**

- `unicodedata.name(c)`
  - 文字 `c` の**名前を返す**

### JSONファイルからデータを読み込むための正しい関数はどれ？

```python
1. json.read()
2. json.parse()
3. json.loads()
4. json.load()
```

**回答**
`json.loads()`

**正解**
`json.load()`

**解説**
**ファイル/文字列からpythonデータへ**
- **ファイルから読み込むとき**
  - `json.load()`

- **文字列から読み込むとき**
  - `json.loads()`

**pythonデータからファイル/文字列へ**

- **ファイルに書き込み**
  - `json.dump(obj, f)`

- **JSON文字列として書き込み**
  - `json.dumps(obj)`

### リストの浅いコピーを作るには？

```python
1. lst.copy()
2. copy.copy(lst)
3. lst[:]
4. 上記すべて
```

**回答**
`copy.copy(lst)`

**正解**
上記すべて

**解説**
- この問題は リストの浅いコピー（shallow copy）を作る方法 を問うものです。

- 浅いコピー は、リスト自体は新しいオブジェクトになるが、リスト内の要素（オブジェクト）は元のリストと同じ参照を共有するコピー。

- `copy.copy(lst)` 
  - 浅いコピーを作成できる

- `lst.copy() `　　　
  - Python 3 の組み込みメソッドで浅いコピーを作成

- `lst[:]` 　　　　
  - スライスによる浅いコピー

**※スライスとは**

- スライス（slice） は、Pythonでリスト・文字列・タプルなどの **一部分を取り出す操作 のこと**

例) `sequence[start:stop:step]`

- start … 開始インデックス（省略すると先頭から）
- stop … 終了インデックス（この位置は含まれない）
- step … 何個飛ばしで取り出すか（省略すると1）

