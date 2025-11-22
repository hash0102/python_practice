# ネストされた構造でも安心
import copy

a = [1, 2, [10, 20]]
b = copy.deepcopy(a)

b[2][0] = 999
# 中にあるリストも別物としてコピーされている
print(a)  # [1, 2, [10, 20]] ← 元は変わらない！
print(b)  # [1, 2, [999, 20]

# IDで確認
print(id(a[2]) == id(b[2]))  # False ← まったく別のリスト！
print('----------------------------------')

# 辞書 + リスト

original = {
    'name': 'Alice',
    'scores': [100, 90, 80]
}

shallow = copy.copy(original)
deep = copy.deepcopy(original)

# 中のリストを変更
shallow['scores'][0] = 0

print(original['scores'])  # [0, 90, 80] ← 影響あり
print(deep['scores'])      # [100, 90, 80] ← 影響なし