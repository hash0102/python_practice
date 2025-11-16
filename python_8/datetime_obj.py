from datetime import datetime

dt = datetime(2025, 8, 2, 14, 30, 15)
print(dt)  # 2025-08-02 14:30:15
print('----------------------------------')

# today
now = datetime.today()
print(now)
print('----------------------------------')

# now
from datetime import datetime, timezone

# タイムゾーン指定なし（ローカルタイム）
now = datetime.now()
print(now)
# UTCを指定
now_utc = datetime.now(timezone.utc)
print(now_utc)
print('----------------------------------')

# utcnow
utc_now = datetime.utcnow()
print(utc_now)
print('----------------------------------')

# date
dt = datetime.now()
print(dt)
print(type(dt))
d = dt.date()
print(d)
print(type(d))
print('----------------------------------')

# time
t = dt.time()
print(t)
print(type(t))
print('----------------------------------')

# isoformat
dt = datetime.now()
print(dt.isoformat())  # 例: 2025-08-02T14:30:15.123456
print('----------------------------------')

# fromisoformat
dt3 = "2025-08-02T14:30:15"
print(dt3)
print(type(dt3))
dt3 = datetime.fromisoformat(dt3)
print(dt3)
print(type(dt3))
print('----------------------------------')

# strftime
dt4 = datetime.now()
print(dt4)
print(type(dt4))
dt4 = dt4.strftime("%Y/%m/%d %H:%M:%S")
print(dt4)
print(type(dt4))
print('----------------------------------')

# strptime
dt5 = "2025-08-02 14:30:15"
print(dt5)
print(type(dt5))
dt5 = datetime.strptime(dt5, "%Y-%m-%d %H:%M:%S")
print(dt5)
print(type(dt5))
print('----------------------------------')

# tzname
from datetime import datetime, timezone

dt = datetime.now(timezone.utc)
print(dt.tzname())  # 'UTC'

dt2 = datetime.now()
print(dt2.tzname())  # None（タイムゾーン情報なし）