import csv

# ファイルを読み込みモードで開く
with open('data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    # reader
    reader = csv.reader(csvfile)
    print(type(reader))
    for row in reader:
        print(row)
print('-' * 30)

# ファイルを書き込みモードで開く
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # writer
    writer = csv.writer(csvfile)
    print(type(writer))

    # ヘッダーを書き込む
    writer.writerow(['Name', 'Age', 'City'])

    # データを1行ずつ書き込む
    writer.writerow(['Alice', 30, 'Tokyo'])
    writer.writerow(['Bob', 25, 'Osaka'])

    # 複数のデータを一度に書き込む
    data = [
        ['Charlie', 35, 'Kyoto'],
        ['David', 40, 'Fukuoka']
    ]
    writer.writerows(data)
print('-' * 30)

# unix Dialect を使用してCSVファイルを読み込む
with open('data2.csv', 'r', newline='') as f:
    reader = csv.reader(f, dialect='unix')
    for row in reader:
        print(row)
print('-' * 30)

# タブ区切りのCSV形式を定義する独自のDialect
csv.register_dialect('mytab', delimiter='\t', quoting=csv.QUOTE_NONE)
# tsvを読み込み
with open('data3.tsv', 'r') as f:
    # 独自の'mytab' Dialectを使用してファイルを読み込む
    reader = csv.reader(f, dialect='mytab')
    for row in reader:
        print(row)
print('-' * 30)

# DictReader
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print(type(reader))
    for row in reader:
        print(row)
print('-' * 30)

# DictWriter

# ヘッダーとして使用するキーのリスト
fieldnames = ['Name', 'Age', 'City']

with open('output2.csv', 'w', newline='') as csvfile:
    # DictWriter
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    print(type(writer))

    # ヘッダー行を書き込む
    writer.writeheader()

    # 辞書
    data_row = {'Name': 'Chris', 'Age': 39, 'City': 'Boston'}

    # writerow
    writer.writerow(data_row)

    # 辞書のリスト
    data_rows = [
        {'Name': 'Alice', 'Age': 30, 'City': 'Tokyo'},
        {'Name': 'Bob', 'Age': 25, 'City': 'Osaka'}
    ]

    # writerows
    writer.writerows(data_rows)