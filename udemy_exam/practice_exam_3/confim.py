lst = [[1, 2], [3, 4]]
copy_lst = lst[:]
copy_lst2 = lst[0:2]

lst[0][0] = 10

print(lst)
print(copy_lst)
print(copy_lst2)