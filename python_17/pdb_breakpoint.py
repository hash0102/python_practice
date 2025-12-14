def my_function(numbers):
    total = 0
    for number in numbers:
        total += number
        # ここでデバッガを起動し、'number'と'total'の値を確認できる
        breakpoint()
    return total

result = my_function([10, 20, 30])
print(result)