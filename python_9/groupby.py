from itertools import groupby

data = 'aaabbcccaaa'

for key, group in groupby(data):
    print(key, list(group))
print('----------------------------------')
# sorted関数でソートしたものをgroupby

data2 = [1,3,2,8,2,1,9,10,2,3,6,9]
sorted_data2 = sorted(data2)

for key, group in groupby(sorted_data2):
    print(key, list(group))
print('----------------------------------')

# 応用：key関数で条件を指定する
data = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']
# 先頭文字でグループ化（事前にソート必須）
data.sort(key=lambda x: x[0])

for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
print('----------------------------------')