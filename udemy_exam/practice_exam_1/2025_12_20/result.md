### 問題2 Pythonで PEP8準拠や潜在的エラーをチェックするツール はどれでしょうか？

```python 
1. Black
2. flake8
3. pip
4. venv
```

**回答**
Black
**正解**
**flake8**

**解説**
- **flake8** は、Pythonコードの**静的解析ツール**
- 目的：PEP8違反（**スペースやインデントのずれなど**）のチェックや、潜在的なエラー（**未使用変数、未定義変数**など）の警告。
- なお、Blackは**コード整形ツール**であり、
pipはパッケージ管理、venvは仮想環境管理を行うツールのため、目的が異なります。

### 文字列 `"2025-10-30 14:45"` を `datetime` オブジェクトに変換する正しい方法は？

1.
```python
datetime.strptime("2025-10-30 14:45", "%Y-%m-%d %H:%M")
```

2. 
```python
datetime.parse("2025-10-30 14:45")
```
3.
```python  
from dateutil import parser; 
parser.parse("2025-10-30 14:45")
```

4. 回答 1と2両方正しい

**回答**
```python
datetime.strptime("2025-10-30 14:45", "%Y-%m-%d %H:%M")
```

**正解**
回答 1と2両方正しい

**解説**
- 「`datetime` オブジェクトに変換する」とは、文字列や数値などのデータを、Python の `datetime` 型（日時を扱う型）に変えることを指します。

**回答1**
```python
datetime.datetime.strptime("2025-10-30 14:45", "%Y-%m-%d %H:%M")
```
- 正解
- 標準ライブラリ
- 日付フォーマットを自分で指定する

**回答2**
```python
from dateutil import parser
parser.parse("2025-10-30 14:45")
```
- 正解
- 外部ライブラリ
- フォーマット指定なしで自動変換

**回答3**
```python
datetime.parse()
```
- 不正解
- `datetime` に `parse()` は存在しない
- 実行するとエラー

### 次のコードの出力として正しいものはどれ？

```python
from urllib.parse import urlparse

result = urlparse("https://example.com/path?x=1#frag")

print(result.scheme)
```

```python
1. "https://"
2. "example.com"
3. "path"
4. "https"
```

**回答**
`"example.com"`

**正解**
`"https"`

**解説**
- `urlparse()` の役割
- Python の `urllib.parse.urlparse()` は、URL を以下のような構造に分解する関数です。


``` python
ParseResult(
    scheme='https',
    netloc='example.com',
    path='/path',
    params='',
    query='x=1',
    fragment='frag'
)
```

**暗号的に安全な乱数を生成するためにはどのモジュールを使うべきか？**

```python
1. hashlib
2. random
3. uuid
4. secrets
```

**回答**
`hashlib`

**正解**
`secrets`

**解説**

`random`： 
- 一般的な乱数生成（シミュレーションやゲーム用）   

`secrets`：
- 暗号的に安全な乱数生成（パスワード・トークン・認証コード）

`hashlib`：
- ハッシュ計算（SHA-256 など）     

`uuid`：
- ユニークな識別子の生成

**ファイルの内容とパーミッション情報も含めてコピーするための関数として正しいものはどれか？** 

```python
1. os.copy()
2. shutil.copyfile()
3. shutil.move()
4. shutil.copy()
```

**回答**
`shutil.copyfile()`

**正解**
`shutil.copy()`

**解説**
- `shutil`モジュールとはPythonの標準ライブラリのひとつで、**ファイルやディレクトリをコピー・移動・削除するための便利な関数**をまとめたモジュールです。
- 名前の由来は “**shell utilities**（シェル操作用ツール）”。
- **os モジュールよりも 高レベルなファイル操作** ができます。

`shutil.copy("source.txt", "destination.txt")`：
- コピー元（source）からコピー先へ（destination）へ内容を複製します。
- **ファイルの内容とパーミッション情報（権限）** も一緒にコピーされます。


`shutil.move()`：
- ファイルやフォルダを移動する関数

`shutil.copyfile()`：
- ファイルの内容をコピーするが、**メタデータ（権限など）はコピーしない**

`os.copy()`：
- **osモジュールにcopy()関数は存在しない**

### 次のコードで、変数`pi`の値を小数点以下2桁で表示するには`?`に入る正しいフォーマット指定子はどれか？

```python
pi = 3.14159
print(f"pi is {pi:?}")
```

```python
1. {pi:2}
2. {pi:2f}
3. {pi:.2f}
4. {pi:.2}
```
**回答**
`{pi:.2}`

**正解**
`{pi:.2f}`

**解説**
- **f 文字列（フォーマット文字列）** では、中かっこの中にフォーマット指定子を使って数値の表示方法を指定できます。

**`{pi:.2f}`**
- `: `
  - フォーマット指定の開始
- `.2`
  - **小数点以下2桁を指定**
- `f`
  - 浮動小数点数（fixed-point） 形式で表示

**`{pi:.2}`**
- 有効桁数2桁の指定（例：3.1E+00）となり、意図と異なる。

**`{pi:2f}`**
- 小数点以下の桁数を指定していないためエラーではないが、幅指定だけになる（例: " 3.141590"）。

**`{pi:2}`**
- 整数の幅指定のような扱いで、浮動小数点表示の制御にはならない。

### 現在の作業ディレクトリ（カレントディレクトリ）の絶対パスを取得する関数はどれか？

```python
1. os.chdir()
2. os.getcwd()
3. os.path()
4. os.listdir()
```

**回答**
`os.chdir()`

**正解**
`os.getcwd()`


**解説**
**`os.path()`**
- **パス操作のモジュール**であり、カレントディレクトリを直接返す関数はありません。
- モジュールであり関数ではないため直接呼び出せない。
- 呼び出す場合は`os.path.関数名()`

**`os.listdir()`**
- 指定したディレクトリの **ファイル・フォルダ一覧を取得**する
- `os.listdir(path='.')`　とすればカレントディレクトリのファイル・フォルダ一覧を取得可能

**`os.chdir()`**
- **カレントディレクトリを変更**する関数
- 取得ではなく設定する用途

### スクリプトに渡されたコマンドライン引数のリストを取得するにはどれを使う？

```python
1. sys.stdin
2. sys.args
3. sys.path
4. sys.argv
```

**回答**
`sys.stdin`

**正解**
`sys.argv`

**解説**
- sysモジュールとは、**システム（Python インタプリタやOS環境）に関する機能を使えるよう**にするものです。

**コマンドライン引数　`sys.argv`**
- スクリプト実行時に一緒に渡す情報 のこと
- Python スクリプトを実行するときに、**プログラム内で使いたい値を渡せる**

**例：**
- スクリプト実行
```bash
python sample.py apple banana 123
```

- スクリプト内

```python
import sys

print(sys.argv)
```

- 出力結果

```python
['sample.py', 'apple', 'banana', '123']

sys.argv[0] → 'sample.py'（スクリプト名）

sys.argv[1] → 'apple'

sys.argv[2] → 'banana'

sys.argv[3] → '123
```


**標準入出力操作 `sys.stdin`, `sys.stdout`, `sys.stderr`**

- 標準入力や標準出力をプログラム内で操作

**Python の検索パス `sys.path`**

- モジュールがどのディレクトリから読み込まれるか確認・変更

**プログラム終了 `sys.exit()`**

- 任意のタイミングでスクリプトを終了

### 次のコードの出力として正しいものはどれ？

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Debug message")

logging.info("Info message")
```
```python
1. 何も出力されない

2. Debug message

3. Info message

4. Debug message
   Info message
```


**回答**
`Debug message`

**正解**
`Info message`

**解説**  
- `logging.basicConfig(level=logging.INFO)` は **ログの出力レベルの設定**です。
- レベルの優先順位（低い順）は、**DEBUG < INFO < WARNING < ERROR < CRITICAL**

`level=logging.INFO `と設定すると：
- `INFO` **以上のレベル**（`INFO, WARNING, ERROR, CRITICAL`）**のログが表示**される
- したがって出力されるのは `"Info message"` のみ。

### リスト `[1,2,3]` を変数 `a,b,c` に展開する正しい書き方は？

```python
1. a,b,c <- [1,2,3]
2. a = b = c = [1,2,3]
3. *a,*b,*c = [1,2,3]
4. a,b,c = [1,2,3]
```

**回答**
`*a,*b,*c = [1,2,3]`

**正解**
`a,b,c = [1,2,3]`

**解説**
- Pythonでは**右辺の要素数と左辺の変数数が一致**すればアンパック可能。

### 今日の日付を取得して、「年・月・日」をそれぞれ表示したいときのコードとして、空欄に入る正しいもはどれか
```python

import datetime

today = datetime.date.________
print(today.year, today.month, today.day)
```

```python 
1. fromtimestamp()
2. today()
3. now()
4. today().date()
```

**回答**
`now()`

**正解**
`today()`

**解説**
- Python の `datetime` モジュールの中には、次のようなクラスや関数が含まれています。
  
```python
datetime（モジュール）
├── date（クラス）：日付を扱う
├── time（クラス）：時刻を扱う
└── datetime（クラス） ：日付と時刻を扱う
```

- つまり、`datetime.date.today()`であれば
  - 最初の `datetime` ：モジュール名
  - 次の `date` ： datetimeモジュール内のクラス名
  - `today()` ： dateクラスのメソッド
- という関係になっています。

### 辞書を見やすく表示するコマンドはどれか？

```python
import pprint
data = {'apple':1, 'banana':2, 'orange':3}
```

```python
1. print(data)
2. pprint.pprint(data)
3. data.pretty()
4. pprint(data)
```

**回答**
`pprint(data)`

**正解**
`pprint.pprint(data)`

**解説**
- `pprint`はPythonの標準ライブラリで、「**pretty print（きれいに表示）**」の略。
- 辞書やリスト、ネストした構造のデータを **見やすい形式で出力**してくれます。
- しかし、この問題のように小さい辞書や短いリストでは、改行やインデントが必要ないので、出力は `print()`と変わりません。

**<回答 3>**
- **`pprint` モジュール自体を呼んでも使えない**
- `モジュール名.メソッド()`の型で呼び出す必要がある。

**<回答 4>**
- 辞書オブジェクトに `pretty()` メソッドは存在しない

### pathlib モジュールを使って、現在の作業ディレクトリを取得する正しいコードはどれ？

```python
1. os.getcwd() 
2. pathlib.path.cwd()
3. Path().cwd()
4. pathlib.Path.cwd()
```

**回答**
`os.getcwd()`

**正解**
`pathlib.Path.cwd()`

**解説**
- `pathlib`モジュールとは、Python 標準ライブラリのひとつで、**ファイルパスをオブジェクトとして扱う**ためのモジュールです。
- `Path.cwd()`は、**現在の作業ディレクトリを `Path`オブジェクトで返します。**

### Blackを使ってPythonコードを整形する基本的なコマンドとして正しいのはどれでしょうか？

``` bash
1. pip black myfile.py
2. python -m black myfile.py
3. python black.run(myfile.py)
4. black install myfile.py
```

**回答**
`pip black myfile.py`

**正解**
`python -m black myfile.py`

- Black は pip でインストールしたあと、ターミナルで以下のように使います。

```python
python -m black myfile.py
```
- `-m` は **module の略**
  - これで `myfile.py` が自動的に整形されます。
- **フォルダ全体を整形**したい場合は、`python -m black .`