import unittest

class TestMyFunction(unittest.TestCase):
    def test_assert(self):
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual("hello", "world")

    def test_assert2(self):
        self.assertTrue(5 > 3)
        self.assertFalse(5 < 3)

    def test_assert3(self):
        a = [1, 2]
        b = a
        c = [1, 2]
        self.assertIs(a, b)    # 同じオブジェクトを参照
        self.assertIsNot(a, c) # 別々のオブジェクト
    
    def test_assert4(self):
        d = None
        self.assertIsNone(d)
        self.assertIsNotNone("not none")

    def test_assert5(self):
        my_list = [1, 2, 3]
        self.assertIn(2, my_list)
        self.assertNotIn(4, my_list)

    def test_assert6(self):
        self.assertIsInstance("hello", str)
        self.assertNotIsInstance(123, str)

    def test_assert7(self):
        def div(a, b):
            return a / b

        # with文を使用する形式
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)

        # callableと引数を指定する形式
        self.assertRaises(ZeroDivisionError, div, 1, 0)