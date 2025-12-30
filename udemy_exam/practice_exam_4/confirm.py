def mix(a, b, c):
    # イミュータブル
    a += (1,)
    # ミュータブル
    b += [1]
    # ミュータブル
    c['x'] = 1
    return a, b, c

t = (0,)
l = [0]
d = {'y': 0}

result = mix(t, l, d)

print(result)
print(t, l, d)