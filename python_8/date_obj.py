from datetime import date

d = date(2025, 8, 2)  # 年、月、日を指定して作成
print(d)  # 2025-08-02
print('----------------------------------')
# today
today = date.today()
print(today) 
print('----------------------------------')
# weekday
print(d.weekday())  # 例: 5（土曜日 → 5）
print('----------------------------------')
# isoweekday
print(d.isoweekday())  # 例: 6（土曜日 → 6）
print('----------------------------------')
# isoformat
print(d.isoformat())  # '2025-08-02'
print('----------------------------------')
# fromisoformat
time = "2025-08-02"
print(type(time))
d = date.fromisoformat(time)
print(d)  # date(2025, 8, 2)
print(type(d))
print('----------------------------------')
d = date(2025, 8, 2)
print(d.strftime("%Y/%m/%d"))        # '2025/08/02'
print(d.strftime("%A"))              # 'Saturday'
print(d.strftime("%Y年%m月%d日"))     # '2025年08月02日'
print('----------------------------------')
d = date.today()

print("今日の日付:", d)
print("曜日 (0=月):", d.weekday())
print("ISO曜日 (1=月):", d.isoweekday())
print("ISO形式文字列:", d.isoformat())

# 文字列から日付へ変換
d2 = date.fromisoformat("2025-08-02")
print("fromisoformat:", d2)

# 書式付き文字列
print("日本語形式:", d.strftime("%Y年%m月%d日")) 
print("曜日（英語）:", d.strftime("%A"))  
print('----------------------------------')