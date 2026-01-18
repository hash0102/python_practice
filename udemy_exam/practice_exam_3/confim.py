lst = [[1, 2], [3, 4]]
copy_lst = lst[:]
copy_lst2 = lst[0:2]

lst[0][0] = 10

print(lst)
print(copy_lst)
print(copy_lst2)

print('-'*30)

import unicodedata

s1 = "ガ"
s2 = "ガ"
print(s1 == s2)

print(unicodedata.normalize("NFC", s1) == unicodedata.normalize("NFC", s2))

s3 = unicodedata.normalize("NFD", s2)
print(len(s3))
for i in s3 :
    print(i)

print('-'*30)

s4 = "ＡＢＣ①２３"
s5 = "ABC123"
print(s4 == s5)
print(unicodedata.normalize("NFKC", s4) == s5)

s6 = unicodedata.normalize("NFKD",s4)
print(len(s6))
for j in s6:
    print(j)
