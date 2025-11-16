import time

t = time.localtime()

print("年:", t.tm_year)
print("月:", t.tm_mon)
print("日:", t.tm_mday)
print("曜日:", t.tm_wday)      # 0 = 月曜
print("通算日:", t.tm_yday)
print("夏時間フラグ:", t.tm_isdst)