### pipとvenvの記述で、誤っているものはどれか。実行環境はUNIX系OSとする。

```python
1. pip freeze > requirement.txt
2. pip install -r requirement.txt
3. pip install -c constrains.txt
4. python -m venv env
```

A. `pip install -c constrains.txt`
- 選択肢3が正解


**1. `pip freeze > requirement.txt`**
- 実行環境にインストールされているパッケージを、**テキストファイルにリストアップ**する際の記述
- パッケージ名とバージョンを合わせてリストアップできる

**2. `pip install -r requirement.txt`**
- 選択肢1で作成したファイルを利用して、**実行環境にパッケージをインストールする際の記述**
- リストアップしたパッケージを、指定のバージョンで一括でインストールできる

**3. `pip install -c constrains.txt`**
- `-r`オプションを利用してパッケージをインストールする際に、**`-c`オプションを使うとパッケージのバージョンに制限をかける**ことができる
- requirement.txtにはバージョンを記載せず、**constrains.txtにバージョンを記載することで制限**する
- -cオプションは「**`pip install -r requirement.txt -c constrains.txt`**」のように、**-rオプションと合わせて使う**
- -cオプションを単独で使うとエラーになる

**4. `python -m venv env`**
- 仮想環境を作成する際の記述
- `-m`オプションは**モジュールを実行する際のオプション**で、この場合は「venv」モジュールを実行して、ディレクトリ名「env」の仮想環境を作成しています。


### デコレーター関数で、functools.wrapsを使って置き換えるものはどれか。

1. 
```python
__name__
__doc__
```

2. 
```python
__repr__
__doc__
```

3. 
```python 
__name__
__call__
```

4. 
```python
__str__
__doc__
```

**A.**
```python
__name__
__doc__
```
- デコレーターを使用すると関数が置き換わるため、**もとの関数の名前やdosctringが失われる**
- 以下の記述の場合、tmp関数をwrapper関数で置き換えているため、「`tmp.__name__`」で関数の名前を確認すると「wrapper」が返る

```python
def deco(func):
    def wrapper(arg):
        func(arg)
        print(arg + 1)
    return wrapper

@deco
def tmp(num):
    print(num)

tmp(10)
```
- そこでfunctools.wrapsを利用する
- 以下のように、1行目でモジュールをインポートして、wrapper関数に「**`@wraps(デコレート対象の関数を受け取る仮引数)`**」を付ける

```python
from functools import wraps

def deco(func):
    @wraps(func)
    def wrapper(arg):
        func(arg)
        print(arg + 1)
    return wrapper

@deco
def tmp(num):
    print(num)

tmp(10)
```
- これで関数の名前（`__name__`）がwrapper関数のものからtmp関数のものに置き換わるため、「`tmp.__name__`」で関数の名前を確認すると「tmp」が返る

- また、**`"""`** で囲ったdosctring（__doc__）があれば、**tmp関数のものに置き換わる**


### 次のクラスに関する説明で、誤っているものはどれか。

```python
class Book:
  def __init__(self, title, price):
    self.title = title
    self.price = price

  def __repr__(self):
    return f'{self.title}'

  def __len__(self):
    return len(self.title)

  def __eq__(self, other):
    return self.price == other.price

# インスタンスは次の2つを生成したものとする。
sample1 = Book('Python', 500)
sample2 = Book('Java', 500)
```


1. `__init__()`メソッドは特殊メソッドの1つである。
2. 「`print(sample1)`」を実行すると「`Python`」が返る。
3. 「`len(sample2)`」を実行すると「4」が返る。
4. 「`sample1 == sample2`」を実行すると「False」が返る。

**A. 「`sample1 == sample2`」を実行すると「False」が返る。**
- クラスで特殊メソッドを記述すると、Pythonの組み込み関数や演算子の処理をカスタマイズできる
- 【選択肢1】
  - インスタンス変数を初期化する`__init__()`メソッドも、特殊メソッドの1つ
- 【選択肢2】
  - `__repr__()`メソッドはprint()関数の内容を変更する
    - ここでは`title`の内容が返るように指定している
- 【選択肢3】
  - `__len__()`メソッドは文字や要素の数を出力
    - ここではtitleの文字数が返るように指定
- 【選択肢4】
  - `__eq__()`メソッドは**比較演算子`==`の処理を変更**
    - ここではpriceの内容が一致していればTrue、不一致であればFalseが返るように指定
  - 選択肢4は「`500 == 500`」の結果を判定しているためTrueが返る

### 本日の日付を文字列で出力したい場合、次の記述の続きとして正しいものはどれか。

```python
from datetime import datetime

now = datetime.now()
```

```python
選択 1
print(f'今日は{%Y年%m月%d日:now}です')
選択 2
print(f'今日は{now:%Y年%m月%d日}です')
選択 3
print(now(f'今日は{%Y年%m月%d日}です'))
選択 4
print((f'今日は{:%Y年%m月%d日}です').now)
```

**A. `print(f'今日は{now:%Y年%m月%d日}です')`**
- 選択肢2が正解
- 選択肢2は「今日は2023年01月01日です」のような出力結果になる
- **f-stringは変数の後ろに「`:`」を付けることで、フォーマットを指定できる**
- 日付型のフォーマットは特殊で、「`%Y-%m-%d %H:%M:%S`」のように **「`%`」を使う**
- フォーマットは他にも、左寄せなどの配置を指定したり、数値の桁数を指定することができる


### 正規表現に関するコードで、結果が「`['03', '1234', '5678']`」にならないものはどれか。

```python
# reモジュールをインポートしているものとする。
選択 1
pattern = re.compile('[-()]')
pattern.split('03-1234-5678')

選択 2
pattern = re.compile('[\s]')
pattern.split('03 1234 5678')

選択 3
pattern = re.compile('\d+')
pattern.findall('03-1234-5678')

選択 4
pattern = re.compile('[^()]')
pattern.findall('03(1234)5678')
```

**A.**
```python
選択 4
pattern = re.compile('[^()]')
pattern.findall('03(1234)5678')
```
- 選択肢4が正解
- reモジュールの`compile()`は、正規表現のオブジェクトを作成する関数
- 作成した正規表現オブジェクトに対して、`split()`や`findall()`などのメソッドを使用して、文字列の分割や検索をする
<br>

- 【選択肢1】
```python
pattern = re.compile('[-()]')
pattern.split('03-1234-5678')
```
- 「`[...]`」は、「`...`」で**指定したいずれかの文字を表す特殊文字**で、ここでは「`-`」「`(`」「`)`」のいずれかで**分割（split）**して、リストを返す
  - 結果は「`['03', '1234', '5678']`」になる
<br>

- 【選択肢2】
```python
pattern = re.compile('\s')
pattern.split('03 1234 5678')
```
- 「`\s`」は**空白文字を表す特殊文字**で、ここでは**空白文字で分割（split）**してリストを返す。
  - 結果は「`['03', '1234', '5678']`」になる
<br>

- 【選択肢3】
``` python
pattern = re.compile('\d+')
pattern.findall('03-1234-5678')
```
- 「`\d+`」は**1文字以上の数字の繰り返しを表す特殊文字**。
  - `findall`は**指定した正規表現にマッチした文字列をリストで返す**。
    - 結果は「`['03', '1234', '5678']`」になる
<br>

- 【選択肢4】
```python
pattern = re.compile('[^()]')
pattern.findall('03(1234)5678')
```
- 「`[^()]`」は、「`(`」と「`)`」以外の文字列を表す
- **ここでは「0312345678」が対象**となり、文字列を1つずつ判定するため、結果は「`['0', '3', '1', '2', '3', '4', '5', '6', '7', '8']`」になる
- 選択肢3の場合は、「`\d+`」で「**1文字以上の数字の繰り返し（まとまり）**」を判定しているため、結果は「['03', '1234', '5678']」になる
- 選択肢3の特殊文字が「`\d+`」ではなく「`\d`」だった場合は、**選択肢4と同じ結果**になる

**正規表現の特殊文字**
```python
\d 数字
\D 数字以外
\s 空白文字
\S 空白文字以外
\w 任意の英数字
\W 英数字以外
. 任意の1文字
^ 先頭
$ 末尾
* 0文字以上の繰り返し
+ 1文字以上の繰り返し
? 0回か1回の繰り返し
{m} m回の繰り返し
{m, n} m回以上、n回以下の繰り返し
[...] 指定したいずれかの文字
[^...] 指定したいずれかの文字以外
```


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
- 例えば正規表現で数字を表す「`\d`」は、それが正規表現の特殊文字であることを明確にするために、本来は「`\\d`」と記述するべきですが、実際は「\d」でも機能する
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

### 次のコードと同じ処理になるものはどれか。
```python
from collections import defaultdict

def func():
    return 0

dd = defaultdict(func)
```

```python
選択 1
dd = defaultdict(0)

選択 2
dd = defaultdict(int)

選択 3
dd = defaultdict(False)

選択 4
dd = defaultdict(None)
```

**A. `dd = defaultdict(int)`**
- 選択肢2が正解
- 辞書は存在しないキーを参照しようとするとエラーになりますが、`collections`モジュールの`defaultdict`を使うと、**存在しないキーを参照したときにデフォルト値を返す**
- 問題文は、`defaultdict`の引数にfunc関数を指定することで、**デフォルト値として0を返す**ように設定している
- 選択肢2のように、`defaultdict`の引数に「`int`」を指定すると、問題文のように**func関数を記述しなくてもデフォルト値が0**になります。

- 問題文や選択肢2のコードに続けて例えば「`dd['a']`」とすると、通常は「dd」に辞書データが代入されていないためエラーになりますが、**「0」が返ります。**
- 他にも、defaultdictの引数に「dict」「list」「set」を指定することで、「空の辞書」「空のリスト」「空の集合」を辞書のデフォルト値として設定できます。

### 次のコードと同じ結果になるものはどれか。

```python
result = []

for i in 'AB':
    for v in 'AB':
        result.append(i + v)

print(result)
```
- 選択肢はすべて、itertoolsモジュールをインポートしているものとする。

```python
選択 1
[i[0] + i[1] for i in itertools.permutations('AB', 2)]

選択 2
[i[0] + i[1] for i in itertools.combinations('AB', 2)]

選択 3
[i[0] + i[1] for i in itertools.product('AB', repeat=2)]

選択 4
[i[0] + i[1] for i in itertools.combinations_with_replacement('AB', 2)]
```

**A. `[i[0] + i[1] for i in itertools.product('AB', repeat=2)]`**
- 選択肢3が正解
- 問題文の結果は「`['AA', 'AB', 'BA', 'BB']`」になる

**【選択肢1】**
```python
[i[0] + i[1] for i in itertools.permutations('AB', 2)]
```
- 結果は`['AB', 'BA']`になります。
- `permutations()`関数は**順列**です。
- 順列とは、**区別可能なn個のものからk個を選んで順に並べます**。
- `permutations()`関数は、**第1引数で出力対象のイテラブルオブジェクト**、**第2引数で出力する長さ**を指定します。
- 選択肢1の場合、ABから2個を選んで順に並べます。
- `AA`などの**重複は出力されません。**

**【選択肢2】**
```python
[i[0] + i[1] for i in itertools.combinations('AB', 2)]
```
- 結果は`['AB']`になります。
- `combinations()`関数は、**重複なしの組み合わせを出力**します。
- `AB`と`BA`のように**同じ要素の組み合わせは出力されません。**

**【選択肢3】**
```python
[i[0] + i[1] for i in itertools.product('AB', repeat=2)]
```
- 結果は問題文と同じで`['AA', 'AB', 'BA', 'BB']`になります。
- `product()`関数は、引数のイテラブルオブジェクトに対して、**すべての組み合わせを返します。**
- デカルト積（直積）と呼ばれており、問題文のネストされた`for`文と同じ結果になります。
- なお、**itertoolsモジュールの各関数は第2引数で出力する長さを指定**しますが、`product()`関数だけは **「`repeat=[n]`」の形式で記述** 

**【選択肢4】**
```python
[i[0] + i[1] for i in itertools.combinations_with_replacement('AB', 2)]
```
- 結果は`['AA', 'AB', 'BB']`になります。
- `combinations_with_replacement()`関数は、**重複ありの組み合わせを出力**します。
- `AB`と`BA`のように**同じ要素の組み合わせは出力されません**

**`permutations()`**
- 重複なし。順番に並べる。

**`combinations()`**
- 重複なし。順番に並べて、同じ組み合わせなし。

**`combinations_with_replacement()`**
- 重複あり。順番に並べて、同じ組み合わせなし。

**`product()`**
- 重複あり。すべての組み合わせを並べる。

### 次のコードを実行した場合、【A】と【B】の結果として正しいものはどれか。
```python 
import tempfile
from pathlib import Path

with tempfile.TemporaryFile() as f:
    p = Path(f.name)
    print(p.exists())  【A】

print(p.exists())  【B】
```

```python
選択 1
【A】 エラーになる
【B】 エラーになる

選択 2
【A】 True
【B】 False

選択 3
【A】 True
【B】 True

選択 4
【A】 True
【B】 エラーになる
```

**A.** 
```python
【A】 エラーになる
【B】 エラーになる
```
- 選択肢1が正解
- `TemporaryFile()`関数で作成した一時ファイルは、名前を持ったファイルとして作成される保証がないため、**`exists()`メソッドで存在を確認することができません。**

- 問題文の場合、【A】はTypeErrorになり、【B】はNameErrorになります。

- `NamedTemporaryFile()`関数を使用すると、**名前が付いたファイルを作成できます。**

- 問題文のTemporaryFile()関数をNamedTemporaryFile()関数に書き換えると、【A】でTrueとなった後、with文を抜けてファイルが閉じられ、【B】でFalseとなります。

### 特定のファイルを除外して、ディレクトリ「`src`」配下のファイルやディレクトリを「`dst`」にまるごとコピーする場合、次のコードの【A】と【B】に記述する関数はどれか。

```python
import shutil

ignore = shutil.【A】('*.txt', '*.jpg')

shutil.【B】('/src', '/dst', ignore=ignore)
```

```python
選択 1
【A】 ignore_patterns
【B】 copydir

選択 2
【A】 exclude
【B】 copydir

選択 3
【A】 ignore_patterns
【B】 copytree

選択 4
【A】 exclude
【B】 copytree
```

**A.**
```python
【A】 ignore_patterns
【B】 copytree
```
- 選択肢3が正解です。
- `copytree()`関数を使用すると、**特定のディレクトリ配下のファイルやディレクトリを、まるごとコピー**できます。
- 問題文では、`ignore_patterns()`関数を使って**拡張子「txt」と「jpg」のファイルを除外**しています。
- `ignore_patterns()`関数で「`ignore`」という呼び出し可能オブジェクトを作成し、`copytree`関数の引数で「`ignore=ignore`」と指定して除外しています。

### 次のコードでCSVファイルを作成する場合、【A】と【B】に記述するものはどれか。

``` python
import csv

data = [
    {'id': 0, 'name': '田中'},
    {'id': 1, 'name': '高橋'},
    {'id': 2, 'name': '佐藤'}
]
 
with open('sample.csv', newline='', mode='w') as f:
    h = ['id', 'name']
    writer = csv.【A】(f, 【B】=h)
    writer.writeheader()
    writer.writerows(data)
```

```python   
選択 1
【A】 DictWriter
【B】 fieldnames

選択 2
【A】 writer
【B】 quotechar

選択 3
【A】 DictWriter
【B】 delimiter

選択 4
【A】 writer
【B】 lineterminater
```

**A.**
```python
選択 1
【A】 DictWriter
【B】 fieldnames
```
- 選択肢1が正解です。
- 辞書データを**CSVファイルに書き込む場合**は、**`DictWriter()`** メソッドを使用します。

- `DictWriter()`メソッドは **`fieldnames`の引数が必須** で、`fieldnames`によって**辞書の値をどのような順番でファイルに書き込むか**指定します。

- 問題文は、`writeheader()`メソッドでヘッダー行を書き込み、`writerows()`メソッドで辞書データを一括で書き込んでいます。
- `fieldnames`の順番を逆にして`['name', 'id']`とすると、作成されるファイルは以下となります。
- 選択肢2と4のように、【A】で`writer()`メソッドを使うと、`writer()`メソッドには **`fieldnames`の引数がないためTypeError**になります。
- また、選択肢2、3、4の【B】は、csvモジュールの **`reader()`関数と`writer()`関数の引数**です。

**`quotechar`**
- シングルクオートなどの引用符の指定

**`delimiter`**
- タブなどの区切り指定

**`lineterminater`**
- 各行の終端文字の指定

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


**`parse_ps()`**
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

### 次のコードをインタープリタで順番に実行する場合、【A】と【B】に記述するものはどれか。

```python
import timeit

def test():
    return sum(range(10))

result = 【A】('test()', 【B】)

print(result)

0.5388089260000015 # 結果
```

``` python
選択 1
【A】 timeit.timeit
【B】 globals=globals()

選択 2
【A】 timeit
【B】 globals=globals()

選択 3
【A】 timeit.timeit
【B】 namespace=globals()

選択 4
【A】 timeit
【B】 namespace=globals()
```

**A.**
```python
【A】 timeit.timeit
【B】 globals=globals()
```

- 選択肢1が正解です。
- 問題文は、`timeit()`メソッドの外（timeitの引数の外）にある関数の実行時間を計測するコードです。
- `timeit`はデフォルトでは**名前空間`timeit`の中（timeitの引数の中）に定義されているコードを実行**します。
- 問題文の場合、`test()`関数は **`timeit`の名前空間の外（`timeit`の引数の外）で定義されている**ため、**「`globals=globals()`」の引数がないとNameErrorが発生します。**
- また、「`timeit.timeit()`」の最初の`timeit`はモジュール名で、`timeit()`はメソッド名です。
- 「`from timeit import timeit`」でインポートすれば、モジュール名を省略して「`timeit()`」だけで実行できます。


### 次のコードで「`P.C ERROR`」の結果を得たい場合、【A】と【B】に記述するものはどれか。


```python

import logging

logger1 = logging.getLogger('【A】')

logger1.setLevel(logging.DEBUG)

h1 = logging.StreamHandler()

h1.setLevel(logging.DEBUG)

h1.setFormatter(logging.Formatter('%(name)s %(levelname)s'))
logger1.addHandler(h1)

logger2 = logging.getLogger('【B】')

logger2.error('msg')
```

```python
選択 1
【A】 P.C
【B】 P.C

選択 2
【A】 P
【B】 C

選択 3
【A】 P
【B】 P.C

選択 4
【A】 C
【B】 P
```

**A.**
```python
【A】 P
【B】 P.C
```
- 選択肢3が正解です。
- ロガーは、階層構造を定義してフォーマッターなどの設定をまとめることができます。
- 階層構造を定義する場合は、`getLogger()`関数の**引数で名前を指定**し、**子のロガーの名前を`（'親.子'）`のようにドットで繋ぎます。**

- 問題文の流れは以下となります。
```python
import logging

logger1 = logging.getLogger('P')
# 親のロガー「logger1」に「P」の名前を設定する。

logger1.setLevel(logging.DEBUG)
# DEBUGレベル以上のログを出力するよう設定する。

h1 = logging.StreamHandler()
# 出力先を標準に設定したハンドラー「h1」を作成する。

h1.setFormatter(logging.Formatter('%(name)s %(levelname)s'))
# ハンドラー「h1」にフォーマッターを設定する。

logger1.addHandler(h1)
# 親のロガー「logger1」にハンドラー「h1」を設定する。

logger2 = logging.getLogger('P.C')
# 子のロガー「logger2」に名前「C」を設定し、親のロガー「logger1」の名前「P」と階層構造にする。

logger2.error('msg')
# 子のロガー「logger2」のログを出力する。
```
- 子のロガーは、**親のロガーのハンドラーとフォーマッターを使って出力**します。

- 問題文では、**子のロガー**（`logger2`）が、**親のロガー**（`logger1`）の設定「`Formatter('%(name)s %(levelname)s')`」を利用するため、結果が「`P.C ERROR`」になります。
- `name`が「`P.C`」に、`levelname`が「`ERROR`」に対応しています。
- 「`h1.setFormatter(logging.Formatter('%(name)s %(levelname)s'))`」の箇所でフォーマッターが設定されていない場合は、「`logger2.error('msg')`」の出力内容である「`msg`」がそのまま出力されます。
- なお、ロギングを構成する部品の説明は以下となります。

```
【ロガー】 ログ出力のインターフェースを提供する
【ハンドラー】 ログの送信先を決定する
【フィルター】 ログのフィルタリング機能を提供する
【フォーマッター】 ログの出力フォーマットを決定する
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
