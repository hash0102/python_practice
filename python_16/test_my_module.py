import unittest
from my_module import my_function # テスト対象の関数をインポート

class TestMyFunction(unittest.TestCase):
    def test_positive_input(self):
        # 肯定的な入力でのテスト
        result = my_function(5)
        self.assertEqual(result, 10) # 結果が10であることを確認

    def test_negative_input(self):
        # 否定的な入力でのテスト
        result = my_function(-2)
        self.assertEqual(result, -4) # 結果が-4であることを確認