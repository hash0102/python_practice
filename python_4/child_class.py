# 例：unittest.TestCaseを継承
import unittest

# unittest.TestCaseを親とした子クラスを定義
class Testsample(unittest.TestCase):
    # unittest.TestCaseが提供するテスト事前準備用メソッドを上書き
    def setUp(self):
        self.target = 'foo'
    
    # 新たなメソッドを定義し、テスト実行対象のメソッドとなる
    def test_upper(self):
        # unittest.TestCaseが提供するassertEqualメソッドを使ってテスト
        self.assertEqual(self.target.upper(), 'FOO')