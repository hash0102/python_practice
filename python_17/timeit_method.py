# Timerクラスを使って、リスト内包表記とforループの実行時間を比較
import timeit

def list_comprehension():
    return [i*i for i in range(1000)]

def for_loop():
    result = []
    for i in range(1000):
        result.append(i*i)
    return result

# Timerインスタンスの作成
# setup引数にfrom __main__ import ...と書くことで、Timerが実行される独立した名前空間で関数が利用可能になる
timer_comp = timeit.Timer('list_comprehension()', 'from __main__ import list_comprehension')
timer_loop = timeit.Timer('for_loop()', 'from __main__ import for_loop')

# timeit()メソッドで合計時間を取得
time_comp = timer_comp.timeit(number=1000)
time_loop = timer_loop.timeit(number=1000)

print(f"リスト内包表記: {time_comp:.6f}秒")
print(f"forループ: {time_loop:.6f}秒")