### 次のコードを実行し特定のエラーですという文字を出力する、【1】に入る正しいものを次の記述の中から選べ

```PYTHON
def func3():
    a = 1
    d = 2

    try:
        print(a + b)
    except 【1】:
        print('特定のエラーです')

func3()
```

```python
1. ValueError
2. TypeError
3. NameError
4. NotImplemented
```

**解答**
`ValueError`

**正解**
`NameError`

**解説**
- 存在しない変数を参照しようとすると`NameError`が発生します。
- `NameError`は、**ローカルまたはグローバル名前空間内で名前が見つからないとき**に発生します。

### PEP 8に従ったPythonのコードにおいて、インデントの正しいスペースを選べ

```python
1. 4スペース
2. 3スペース
3. 2スペース
4. タブ文字
```

**解答**
2スペース

**正解**
4スペース

### 以下のコードの実行結果で正しいものを選べ

```python
# oの後にはスペースがあります
target = "Hello 🌍!"
print(target.find("🌍"))
```

```python
1. 6
2. 5
3. -1
4. エラーが発生する
```

**解答**
5

**正解**
6


### 次の【1】に入るコードの実行結果として、 エラーとなる記述を選べ

```python
def user_information(name, age, email):
    return {
        'name': name,
        'age': age,
        'email': email
    }
【1】
```

```python
1. user_information(“taro”, 20, “taro@example.com”)
2. user_information(“taro”, “taro@example.com”, 20)
3. user_information(“taro@example.com”, 20, “taro”)
4. user_information(“taro”, 20, “taro@example.com”, “tokyo”)
```

**解答**
`user_information(“taro”, 20, “taro@example.com”)`

**正解**
`user_information(“taro”, 20, “taro@example.com”, “tokyo”)`

### 次のコードを実行した結果から、【1】に入る正しいものを次の記述の中から選べ

```python
def join_char(*args):
    word = ""
    for i in args:
        word += i
    return word

t_word = ("a", "b", "c")
【1】

[実行結果]
abc
```

```python
1. print(join_char(*t_word))
2. print(join_char(t_word))
3. print(join_char(**t_word))
4. print(join_char(+t_word))
```

**解答**
`print(join_char(**t_word))`

**正解**
`print(join_char(*t_word))`


### shutil モジュールの関数のうち、ソースファイルと目的ファイルの両方のパスを指定し、さらにファイルのメタデータ（最終アクセス時間と最終変更時間）もコピーする関数を選べ

```python
1. shutil.copy2(src, dst)
2. shutil.move(src, dst)
3. shutil.copy(src, dst)
4. shutil.copyfile(src, dst)
```

**解答**
`shutil.copyfile(src, dst)`

**正解**
`shutil.copy2(src, dst)`


### 次のコードの実行結果を選べ

```python
import timeit

def my_function():
    return [x*2 for x in range(1000)]

timeit.timeit('my_function()', globals=globals())
```

```python
1. my_functionの1000000回実行にかかった時間を示す
2. エラーが発生する
3. globals関数は存在しないため、エラーになる
4. ‘my_function()’文字列の実行時間を示す
```

**解答**
エラーが発生する

**正解**
my_functionの1000000回実行にかかった時間を示す

**解説**
- `timeit.timeit()` は**デフォルトで100万回**（1_000_000回）my_function() を実行
  - その**合計実行時間（秒） を返します**

