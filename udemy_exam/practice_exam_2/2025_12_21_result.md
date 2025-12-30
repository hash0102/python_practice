### 次の関数に対して doctest を動かしたとき、テストが成功する出力はどれ？

```python
def add(a, b):
    """
    >>> add(2, 3)
    5
    """
    return a + b
```

```python
1. 出力が異なるため失敗
2. 成功（すべてOK）
3. doctestでは引数が渡せない
4. TypeError が発生
```

**回答**
出力が異なるため失敗

**正解**
成功（すべてOK）

**解説**
**`doctest`の仕組み**
- `doctest` は docstring 内の`>>>`から始まる行を **Pythonコードとして実行し、その直後の行に書かれた期待出力と比較**します。
  - 上記の場合、`>>> add(2, 3)` が実行されると add 関数が呼ばれ、戻り値として 5 が返ります。
**期待出力との一致**
- docstring 内では 5 と書かれており、関数の実際の返り値も 5 です。
- そのため、doctest は期待値と一致したと判断し、テストは成功します。


### 次のコードの意味として正しいものはどれ？

```python
import timeit

print(timeit.timeit("a = 10 * 5", number=1000000))
```

```python
1. 実行結果を数値として返す
2. コードを100万回実行し、平均時間を返す
3. 1回だけ実行した時間を返す
4. コードを100万回実行し、合計実行時間を返す
```

**回答**
コードを100万回実行し、平均時間を返す

**正解**
コードを100万回実行し、合計実行時間を返す

**解説**
- timeit モジュールは、**プログラムの短いコードの一部の実行時間を測る**ためのツールの標準ライブラリです。

- `timeit.timeit()`：
  - **合計実行時間（秒）** を返す関数
- `"a = 10 * 5"`：
  - 計測対象のコード（文字列で指定）
- `number=1000000`：
  - 100万回繰り返して実行する回数を指定


### ディレクトリを再帰的に削除する関数はどれ？

```python
1. shutil.rmtree()
2. os.rmdir()
3. shutil.removedirs()
4. os.remove()
```

**回答**
`os.rmdir()`

**正解**
`shutil.rmtree()`

**解説**
`os.remove()`
- ファイルを削除する関数
  - ディレクトリは削除できない

`os.rmdir()`
- 空のディレクトリを削除する
  - 中身があるディレクトリは削除できない

`shutil.rmtree()`
- ディレクトリとその中の**全てのファイル・サブディレクトリを再帰的に削除**する
  - 大量のファイルが入ったフォルダをまとめて削除したいときに便利

`shutil.removedirs()`
- **指定したディレクトリと その親ディレクトリを空の場合**にまとめて削除
  - **中身があるディレクトリは削除できない**
  
### 辞書内包表記の正しい例は？

```python
1. [x:x*2 for x in range(3)]
2. {x:x*2 for x in range(3)}
3. (x:x*2 for x in range(3))
4. {x*2 for x in range(3)}
```

**回答**
`[x:x*2 for x in range(3)]`

**正解**
`{x:x*2 for x in range(3)}`

**解説**
```python
{x:x*2 for x in range(3)} ：辞書内包表記

{x*2 for x in range(3)} ：セット内包表記

[x*2 for x in range(3)] ：リスト内包表記

(x*2 for x in range(3)) ：ジェネレータ内包表記
```

### 次のコードの mocked_func 呼び出し回数を確認する正しい方法はどれ？

```python
from unittest.mock import Mock

mocked_func = Mock()
mocked_func()
mocked_func()
```

```python
1. mocked_func.calls
2. mocked_func.called_times
3. mocked_func.call_count
4. mocked_func.count()
```

**解説**
- モック（mock）とは、「本物のオブジェクトの代わりに使うテスト用の仮のオブジェクト」です。
- たとえば：
  - ネットワーク通信をする関数
  - データベースを操作する関数
  - 時間や外部 API に依存する処理
- こうした「外部に依存する処理」をそのままテストすると遅い・不安定になりがちです。
- そこで「モック」に置き換えて、します。

- `unittest.mock.Mock` オブジェクトは、**関数やメソッドの呼び出し状況を記録**してくれます。
- その中でも `call_count` 属性は「**そのモックが何回呼ばれたか**」を表します。
- `mocked_func` が 2 回呼ばれているので `call_count` は 2 になります。


### Path オブジェクト `p = Path("example.txt")` に対して、そのファイルが存在するか確認するにはどれを使う？

```python
1. os.exists(p)
2. p.isopen()
3. p.exists()
4. p.isfile()
```

**解説**
`Path.exists()`
- **Pathオブジェクトが指すファイルやディレクトリが存在するかを確認**できる
  - 存在すれば True、存在しなければ False を返す

`p.isfile() `
- 存在している ファイルかどうか を確認するメソッドは正しくは`p.is_file()`

`os.exists(p)` 
- `os.path.exists(p)` と書く必要がある（**`os.exists` は存在しない**）

`p.isopen()` 
- Path に存在しないメソッド

### 標準ライブラリだけを使って、アメリカ・ニューヨークのタイムゾーンで現在日時を取得するコードとして正しいのはどれでしょう？

1. 
```python
import time

dt = time.now("America/New_York")
```

2. 
```python
from datetime import datetime
from pytz import timezone

dt = datetime.now(timezone("America/New_York"))
```

3. 
```python
from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime.now(ZoneInfo("America/New_York"))
```

4. 
```python
from datetime import datetime

dt = datetime.now("America/New_York")
```

**回答**
```python
from datetime import datetime

dt = datetime.now("America/New_York")
```

**正解**
```python
from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime.now(ZoneInfo("America/New_York"))
```

**解説**
- Python 3.9以降では、`zoneinfo`モジュールを使ってタイムゾーン対応が可能
- `datetime.now(ZoneInfo("タイムゾーン名"))` とすると、**そのタイムゾーンの現在日時を取得**できる


**回答2**
- 外部ライブラリ`pytz` を使う古い方法、最近の Python では標準ライブラリの `zoneinfo `が推奨

**回答4**
- **`datetime.now()` に文字列は渡せない。**
  - エラーになる

**回答1**
- `time` モジュールには**タイムゾーン指定はできない。**
  - `time.now()` も存在しない

### リストを降順でソートするにはどれ？
```python
nums = [3,1,4]
```

```python
1. AとB両方正しい
2. sorted(nums, reverse=True)
3. sorted(nums, reverse=False)
4. nums.sort(reverse=True)
```

**解説**
**`sorted()` と `list.sort()` の違い**

`sorted(iterable, reverse=True/False) `
- 元のリストを変更せず、新しいソート済みリストを返す

`list.sort(reverse=True/False) `
- 元のリストをその場でソート（破壊的変更）

### 次のうち、Python の`dataclasses`モジュールを使って正しくデータクラスを定義しているものはどれ？

1. 
```python
@dataclass
def Person(name: str, age: int):
    pass
```

2. 
```python
@dataclass
class Person(name, age):
    pass
```

3. 
```python
@dataclass
Person(name: str, age: int)
```

4. 
```python
@dataclass
class Person:
    name: str
    age: int
```

**回答**
```python
@dataclass
class Person(name, age):
    pass
```

**正解**
```python
@dataclass
class Person:
    name: str
    age: int
```

**解説**
- `dataclass` は **データを保持するシンプルなクラス**を簡単に作るためのデコレーターです。

- デコレーターは関数にもクラスにも付けられるものがありますが、dataclass は クラス専用デコレーターです。

**dataclass の基本的な書き方**
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

**ポイント**
- クラス定義の括弧には親クラスを書く（継承する場合）。
- `class Person:` のように**空なら括弧は不要** 
- フィールド（属性）はクラス内にアノテーションで書く
  - `name: str `のように型注釈を使う
- 直接 `class Person(name, age):` のように書いてはいけない

### 次のコードを実行したときの出力として正しいものはどれでしょう？

```python
import unicodedata

print(unicodedata.name("あ"))
```

```python
1. エラー
2. "U+3042"
3. "A"
4."HIRAGANA LETTER A"
```

**回答**
`"U+3042"`

**正解**
`"HIRAGANA LETTER A"`

**解説**
- Python の標準ライブラリ`unicodedata`は、**文字の Unicodeに関する情報を扱う**ためのモジュールです。
- `unicodedata.name(c)`は、指定した文字`c`の **Unicode名（正式名称）** を返します。
- `"U+3042"`は、**Unicodeコードポイント**。
  - `ord()`で得た値を整形することで `"U+xxxx"` 形式を作れます。

### 標準出力ではなく標準エラー出力に文字列を表示する正しい方法はどれ？

```python
1. sys.print("Error occurred")
2. print("Error occurred", file=sys.stderr)
3. sys.stderr("Error occurred")
4. print("Error occurred")
```

**回答**
`sys.stderr("Error occurred")`

**正解**
`print("Error occurred", file=sys.stderr)`


**解説**
`print("Error occurred", file=sys.stderr)`
- このコードは 「`Error occurred`」という文字列を標準エラー出力（`stderr`）に書き込む」 という意味です。

**stdout**
- 正式名称：**standard output**
- 意味： **標準出力**

**stderr**
- 正式名称：**standard error**
- 意味：**標準エラー出力**

### 次のコードを実行したとき、出力結果は何でしょう？

```python
import bisect

nums = [1, 3, 5, 7]
print(bisect.bisect_left(nums, 4))
```

```python
A. 8
B. 1
C. 4
D. 2
```

**回答**
4

**正解**
2

**解説**
- `bisect.bisect_left(a, x)` は、**ソート済みリスト `a` に `x` を挿入するならどの位置が適切か**を返す関数です。
- 左側から見て、`x` が入る最初の位置を返します。

- `nums` の中で 4 を入れるとすると、**3 と 5 の間**に入るのが自然です。
- インデックスは **0,1,2,3** なので、**4を入れる位置は2** になります。

- 値がリストに 存在しない場合は`bisect_left`と `bisect_right`は同じ結果
  - 値がリストに存在する場合に出力が異なる。
  - `bisect_left　`
    - x と同じ値があれば左側に挿入
  - `bisect_right　`
    - x と同じ値があれば右側に挿入


