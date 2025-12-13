def my_complex_function(a, b):
    """
    複数の引数を扱う関数の例。

    >>> a = 1
    >>> b = 2
    >>> my_complex_function(a, b)
    3
    """
    return a + b

import doctest

def my_function(x):
    """
    >>> my_function(2)
    3
    """
    return x + 1

if __name__ == '__main__':
    doctest.testmod()
    doctest.testmod(verbose=True)