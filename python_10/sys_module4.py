import sys

if sys.version_info >= (3, 10):
    print(sys.version_info)
    print("Python 3.10 以上で動作")
else:
    print("古いバージョンの Python")
print('----------------------------------')

# 属性アクセスとインデックスアクセス
print(sys.version_info.major)   # 3
print(sys.version_info[0])      # 3（同じ意味）
print('----------------------------------')

# releaselevel
print(sys.version_info.releaselevel)
if sys.version_info.releaselevel != 'final':
    print("まだ正式リリースではありません。")