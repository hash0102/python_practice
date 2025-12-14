import timeit

def list_comprehension():
    return [i*i for i in range(1000)]

# Timerインスタンスの作成
timer_comp = timeit.Timer('list_comprehension()', 'from __main__ import list_comprehension')

# repeat()メソッドで5回の測定結果を取得
results = timer_comp.repeat(repeat=5, number=10000)

# 最も速い時間を取得
best_time = min(results)

print(f"ベストタイム: {best_time:.6f}秒")