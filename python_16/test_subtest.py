# subTestを使用する例
import unittest

class MyTest(unittest.TestCase):
    def test_addition_multiple_inputs(self):
        test_cases = [(1, 2, 3), (3, 4, 7), (5, 5, 11)] # 最後のケースは失敗する
        for a, b, expected in test_cases:
            # subTestを使用することで、各ループが個別のテストとして扱われる
            with self.subTest(a=a, b=b, expected=expected):
                result = a + b
                self.assertEqual(result, expected)