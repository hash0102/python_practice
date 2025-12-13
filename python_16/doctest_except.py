# int型にhelloを渡しているためエラー
def my_function(x):
    """
    >>> my_function("hello")
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "int") to str

    >>> my_function(1)
    2
    """
    return x + 1


# 複数の例外を扱う
def check_value(value):
    """
    引数の型と値によって異なる例外を発生させます。

    >>> check_value("text")
    Traceback (most recent call last):
      ...
    TypeError: 'int' or 'float' expected

    >>> check_value(0)
    Traceback (most recent call last):
      ...
    ValueError: value must be non-zero

    >>> check_value(10)
    10
    """
    if not isinstance(value, (int, float)):
        raise TypeError("'int' or 'float' expected")
    if value == 0:
        raise ValueError("value must be non-zero")
    return value

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)