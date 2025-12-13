# run_tests.py
import doctest

if __name__ == '__main__':
    doctest.testfile("example.txt", verbose=True)
    doctest.testfile("example.md", verbose=True)