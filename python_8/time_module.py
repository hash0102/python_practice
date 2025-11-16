import time

# time
t = time.time()
print(t)  # 例: 1722582353.123456（float型）
print('---------------------------------------')

# gmtime
t = time.time()        # 現在のUNIX時間
print(type(t))
utc = time.gmtime(t)   # UTC の struct_time に変換
print(utc)
print(type(utc))

# secs指定
secs = 0           # 特定のUNIX時間を秒で指定
utc2 = time.gmtime(secs)     # UTC に変換
# 0を指定したため、1970年1/1日になっている
print(utc2)
print('---------------------------------------')

# localtime
t2 = time.time()        
t2 = time.localtime(t2)
print(t2)
print(type(t2))
print('----------------------------------')

# strfitime
t3 = time.localtime()
print(t3)
print(type(t3))
t3 = time.strftime("%Y-%m-%d %H:%M:%S", t3)  # '2025-08-02 15:32:33'
print(t3)
print(type(t3))
print('----------------------------------')