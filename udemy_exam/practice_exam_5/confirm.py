text = "apple,banana,orange"

parts = text.split(",")
print(parts)

index = text.find("banana")
print(index)
index2 = text.find("pp")
print(index2)
index3 = text.find("e")
print(index3)



if text.startswith("apple") and index != -1:

    result = "-".join(parts)

else:

    result = text



print(result)

print('-'*30)

import re



pattern = re.compile(r"(?P<letters>[A-Za-z]+)(?P<digits>\d+)")

text = "ID12 CODE345"



m = pattern.search(text)


print(m.group())
print(m.group(1))
print(m.group("digits"))
print(m.groups())
print(m.groupdict())
print(m.expand("{letters}-{digits}"))

print('-'*30)

m2 = pattern.match(text)


print(m2.group())
print(m2.group(1))
print(m2.group("digits"))
print(m2.groups())
print(m2.groupdict())
print(m2.expand("{letters}-{digits}"))

print('-'*30)

s1 = "こんにちは"
s2 = "一二三四" 
s3 = "Python3!"
s4 = "Python"

print(s1.isalpha())
print(s2.isnumeric())
print(s3.isalnum())
print(s4.isupper())