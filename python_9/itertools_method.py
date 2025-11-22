from itertools import product

# product()
# すべての組み合わせを生成
print(list(product([1, 2], ['a', 'b'])))

# repeatを指定する場合
# [0,1]を3つ使用して組み合わせ
print(list(product([0, 1], repeat=3)))
print('----------------------------------')

from itertools import permutations
# ABCの中の2つを使用し、順列を生成
print(list(permutations('ABC', 2)))
print('----------------------------------')

# combinations

from itertools import combinations

print(list(combinations('ABC', 2)))

# combinations_with_replacement
from itertools import combinations_with_replacement

print(list(combinations_with_replacement('ABC', 2)))
