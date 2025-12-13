# 例：２の乗数を返す関数

# 通常の関数
def multiplier(values):
    ret = []
    for i in values:
        ret.append(2 ** i)
    return ret

ret = multiplier([0,1,2,3,4,5])
print(type(ret))

for i in ret:
	print(i)

print('-' * 30)

# ジェネレーター
def multiplier2(values):
    for i in values:
        yield 2 ** i

ret2 = multiplier2([0,1,2,3,4,5])
print(type(ret2))

for i in ret2:
	print(i)

print('-' * 30)

# ジェネレーターでnext関数を使用
def multiplier(): #引数がなく無限に繰り返されるジェネレーター
    num = 1
    while True:
        # 結果を返して一時停止
        yield num
        # 次の呼び出しで実行される
        num *= 2

# 最初の呼び出し 
gen = multiplier()

# ジェネレーターオブジェクトが返される
print(gen)

# 値を取得
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print('-' * 30)

# list()関数を使用してリストに変換する
def multiplier(values):
    for i in values:
        # yieldを使って結果を返す
        yield 2 ** i

values = [0, 1, 2, 3, 4, 5]

ret3 = multiplier(values)
print(ret3)
print(type(ret3))
# listを使用してジェネレーターオブジェクトを変換
ret4 = list(ret3)
print(ret4)
print(type(ret4))
print('-' * 30)


# 大きいファイルの処理にジェネレーターを使用
def text_retrieve(text):
    with open('genertor_sample.txt', 'r', encoding="utf-8") as f:
        for row in f:
            # 引数で指定された文字列を含む場合に値を返す
            if text in row:
                yield row

# 東京という文字が含まれる行の取得
for txt in text_retrieve('東京'):
    # 対象の行に対して別の処理が行われたあとにファイル読み込みループが再開される。
    print(txt)
print('-' * 30)