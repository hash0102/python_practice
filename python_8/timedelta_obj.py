from datetime import timedelta,datetime

delta = timedelta(days=2, hours=3, minutes=30)
print(delta)  # 2 days, 3:30:00
print('---------------------------------------')

# 日時と組み合わせる
now = datetime.now()
print("現在:", now)

# 3日後
three_days_later = now + timedelta(days=3)
print("3日後:", three_days_later)

# 2時間前
two_hours_ago = now - timedelta(hours=2)
print("2時間前:", two_hours_ago)
print('---------------------------------------')

# timedelta 同士の演算
td1 = timedelta(days=3, hours=5)
td2 = timedelta(days=1, hours=2)

diff = td1 - td2
print(diff)  # 2 days, 3:00:00
print('---------------------------------------')

# 属性でアクセス
delta = timedelta(days=2, hours=4, minutes=30)
print("日:", delta.days)                    # 2
print("秒:", delta.seconds)                 # 16200（= 4h * 3600 + 30min * 60）
print("合計秒:", delta.total_seconds())     # 189000.0
print('---------------------------------------')

# 比較演算も可能
td1 = timedelta(days=1)
td2 = timedelta(hours=12)

print(td1 > td2)  # True
print('---------------------------------------')

# マイナスの値もOK
td = timedelta(days=-1, hours=3)
print(td)  # -1 day, 3:00:00
print('---------------------------------------')