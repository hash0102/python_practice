from datetime import time

t = time(14, 30, 15)  # 14時30分15秒
print(t)  # 14:30:15
print('----------------------------------')

# isoformat
t = time(14, 30, 15)
print(t.isoformat())  # '14:30:15'
# マイクロ秒やタイムゾーン情報がある場合も含めて表示される
t2 = time(14, 30, 15, 123456)
print(t2.isoformat())  # '14:30:15.123456'
print('----------------------------------')

# fromisoformat
t3 = "14:30:15"
print(type(t3))
t3 = time.fromisoformat(t3)
print(t3)  # 14:30:15
print(type(t3))

t4 = "14:30:15.123456"
print(type(t4))
t4 = time.fromisoformat(t4)
print(t4)  # 14:30:15.123456
print(type(t4))
print('----------------------------------')

# strftime
t5 = time(14, 30, 15)
print(t5.strftime("%H:%M:%S"))        # '14:30:15'
print(t5.strftime("%I:%M %p"))        # '02:30 PM'
print('----------------------------------')

# tzname
t6 = time(14, 30)
print(t6.tzname())  # None（タイムゾーンなし）

# タイムゾーンありの場合（例: UTC）
from datetime import timezone
t7 = time(14, 30, tzinfo=timezone.utc)
print(t7.tzname())  # 'UTC'
print('----------------------------------')
