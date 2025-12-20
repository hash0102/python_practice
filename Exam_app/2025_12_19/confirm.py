import re
import itertools

pattern = re.compile('[-()]')
print(pattern.split('03-1234-5678'))
print(pattern.split('(03)(1234)(5678)'))
print('-'*30)

pattern2 = re.compile('[\s]')
print(pattern2.split('03 1234 5678'))

# 数字・アルファベット・記号など全部にマッチ
pattern2 = re.compile('[\S]')
print(pattern2.split('03 1234 5678'))
print('-'*30)

pattern3 = re.compile('\d+')
print(pattern3.findall('03-1234-5678'))
# 数字出ない1文字以上の繰り返しにマッチした値を返す
pattern3 = re.compile('\D+')
print(pattern3.findall('03-1234-5678'))
print('-'*30)

pattern4 = re.compile('[^()]')
print(pattern4.findall('03(1234)5678'))
pattern4 = re.compile('[()]')
print(pattern4.findall('03(1234)5678'))
print('-'*30)

pattern5 = re.compile('5678$')
print(pattern5.findall('03(1234)5678'))

pattern6 = re.compile('5.')
print(pattern6.findall('03(1234)5678'))

print('-'*30)

obj = re.match(r'(\d+)-(\d+)-(\d+)', '03-1234-5678')
print(obj.group(1))
print(obj[2][2])

print('-'*30)

print(list(itertools.permutations('AB', 2)))
print(list(itertools.combinations('AB', 2)))
print(list(itertools.product('AB', repeat=2)))
print(list( itertools.combinations_with_replacement('AB', 2)))