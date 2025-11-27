# breakpointの使用例
def my_func():
    x = 42
    breakpoint()  # ここでデバッガ起動
    print(f"x = {x}")

# my_func()

import sys

def fake_debug(*args, **kwargs):
    print("[DEBUG] breakpointが呼び出されました")
# sys.breakpointhook を上書き
sys.breakpointhook = fake_debug

breakpoint()  # => [DEBUG] breakpointが呼び出されました

# breakpoint() に引数を渡すと、breakpointhook にも渡される。
def my_hook(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

sys.breakpointhook = my_hook

breakpoint(1, 2, mode="custom")