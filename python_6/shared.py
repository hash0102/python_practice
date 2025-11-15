#実行結果を出力する関数 
def exe_func(string,func, *args):
    if args:
        if len(args) == 1:
            print(F'\"{string}\".{func.__name__}({args[0]})の実行結果：{func(args[0])}')
        else:
            print(F'\"{string}\".{func.__name__}{args}の実行結果：{func(*args)}')
    else:
        print(F'\"{string}\".{func.__name__}()の実行結果：{func()}')
    print('------------------------------------------------------')


def re_result(func, *args, flags=None):
    if len(args) == 1:
            print(F'pattern.{func.__name__}({args[0]})の実行結果：{func(args[0])}')
    if flags is not None:
        print(f're.{func.__name__}{args}の実行結果：{func(*args, flags=flags)}')
    else:
        print(f're.{func.__name__}{args}の実行結果：{func(*args)}')
    print('------------------------------------------------------')
