## 間違えた個所

#### 以下のコードの実行結果で正しいものを選べ
``` python
class MyObject:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'MyObject: {self.name}'

obj = MyObject('test')
print(obj)
```

``` python
1. MyObject: test
2. <main.MyObject object at 0x10d418160>
3. test
4. None
```

**A.`MyObject: test`**
- このコードでは、`__str__`メソッドをオーバーライドしています。
  - **このメソッドは`print`関数や`str()`内置関数によって呼び出されます。**

※`__repr__`は**スクリプト実行では呼ばれず**、REPL（対話環境）では **`__repr__`** が呼ばれる
```bash
$ python -i confirm.py
__str__: test
>>> MyObject(name='test')
__repr__: test
>>>
```

#### 次のコードを実行し特定のエラーですという文字を出力する、【1】に入る正しいものを次の記述の中から選べ

``` python
def func3():
    a = 1
    d = 2

    try:
        print(a + b)
    except 【1】:
        print('特定のエラーです')

func3()
```

``` python
1. ValueError
2. TypeError
3. NameError
4. NotImplemented
```

**A.`NameError`**
- `b` が定義されていないから **`NameError`**

#### 以下のコードの実行結果で正しいものを選べ
``` python
import io

s = io.StringIO()
s.write('ham\n')
s.seek(0)
s.write('egg')

print(s.getvalue())
```

#### 次のコードを実行したとき、出力として正しいものを選びなさい。

```python
import io

s = io.StringIO()
s.write('ham\n')
s.seek(0)
s.write('egg')

print(s.getvalue())
```
```python
1. ham\negg
2. egg\n
3. ham
4. egg
```
**A. `egg\n`**
- StringIO は 現在のカーソル位置から上書き
- **`seek(0)` により先頭に戻る**
- 'ham' の3文字が 'egg' に置き換わる
- **改行 \n は残る**
 
**ポイント**
- `StringIO.write()` は追記ではなく「**上書き**」

**次のコードを実行した結果として正しいものを選びなさい**

```python
from urllib import parse

query = 'key1=value1&key1=value2&key2=value3'
print(parse.parse_qsl(query))
```

```python
1. {'key1': 'value2', 'key2': 'value3'}
2. {'key1': ['value1', 'value2'], 'key2': ['value3']}
3. [('key1', 'value1'), ('key1', 'value2'), ('key2', 'value3')]
4. [('key1', 'value2'), ('key2', 'value3')]
```

**A. `[('key1', 'value1'), ('key1', 'value2'), ('key2', 'value3')]`**

- `parse_qsl` は **query string list**
- 戻り値は **リスト**
- 同じキーがあっても 順序を保って全て残る

**比較**
```python
parse.parse_qs(query)
# {'key1': ['value1', 'value2'], 'key2': ['value3']}
```

#### Pythonにおける try 文の正しい構文の順序を選びなさい。

```python
1 .
try
finally
except
else

2.
try
except
finally
else

3.
try
except
else
finally

4.
try
else
except
finally
```

**A.**

```python
try
except
else
finally
```
- **else は 例外が発生しなかった場合のみ**
- finally は 必ず最後に実行
- try → except → else → finally

#### セキュリティ用途に適した 16進数文字列のトークン を生成する関数を選びなさい

```python
1. token_bytes
2. token_hex
3. hex_token
4. token_string
```

**A. `token_hex`**
- `token_hex(n)`:
  - nバイトの安全な乱数を16進文字列で返す
- 認証トークン・セッションID向け


#### 次のコードで 
#### `{'address': 'tokyo', 'name': 'taro', 'age': 20}` 
#### を出力する正しい呼び出しを選びなさい。

```python
def attach_custom_dict(**kwargs):
    default_dict = {'address': 'tokyo'}
    for key, value in kwargs.items():
        default_dict[key] = value
    return default_dict

user = {'name': 'taro', 'age': 20}
```

```python
1. attach_custom_dict(user)
2. attach_custom_dict(*user)
3. attach_custom_dict(**user)
4. attach_custom_dict(kwargs=user)
```

**A. `attach_custom_dict(**user)`**
- 関数側が `**kwargs`
- **呼び出し側も `**` で辞書を展開する必要あり**

#### 次のコードの説明として正しいものを選びなさい。

```python
from pathlib import Path
p = Path('.')
list(p.glob('*.log'))
```

```python
1. .log ファイルを削除する
2. .log ファイルを1つ取得する
3. .log ファイルの一覧を取得する
4. .log ファイルを作成する
```

**A. `.log `ファイルの一覧を取得する**
- `glob` は **条件に一致するファイルを列挙**
- 戻り値は**イテレータ** → `list()` で一覧化

#### 次のコードの `result` の型として正しいものを選びなさい。
```pytnon 
result = (x ** 2 for x in range(5))
```

```python
1. list
2. tuple
3. generator
4. set
```

**A. `generator`**
- **`()` + `for` = ジェネレータ式**
- 即時評価されず、必要な分だけ計算