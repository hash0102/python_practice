import pdb

def my_function(x, y):
    result = x + y
    pdb.set_trace() # ここでデバッガが起動します
    final_result = result * 2
    return final_result

my_function(5, 10)