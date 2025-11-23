import unittest
from io import StringIO
import sys

def greet(name):
    print(f"Hello, {name}!")

class TestGreet(unittest.TestCase):
    def test_greet_output(self):
        saved_stdout = sys.stdout  # 元のstdoutを保存
        try:
            fake_stdout = StringIO()
            sys.stdout = fake_stdout  # 標準出力をStringIOに差し替え

            greet("Alice")  # 関数を実行（printがStringIOに出力される）

            # 実行した関数の値を取得
            output = fake_stdout.getvalue()
            # 実行した値が"Hello, Alice!"かどうかをテスト
            self.assertEqual(output.strip(), "Hello, Alice!")
        finally:
            sys.stdout = saved_stdout  # stdoutを元に戻す