# `unittest.TestCase` の`setUp`メソッドを共通化する例
import unittest
import pathlib


class TestBase(unittest.TestCase):
    # 共通化する初期化処理メソッド定義
    def setUp(self):
        # テストに利用する共通の設定を定義
        self.data_path = pathlib.Path('/tmp/data')
    
    # 共通で使う後処理メソッドを定義
    def deftearDown(self):
        for p in self.data_path.iterdir():
            # setUp()で作ったファイルを削除
            p.unlink()

# 上記のTestBaseを親クラスとした子クラスを定義
class TestSample1(TestBase):
    # 初期化処理メソッドを上書き
    def setUp(self):
        # super関数で親クラスを呼び出し、親クラスのSetUpメソッド実行
        super().setUp()
        p1 = self.data_path / 'sample1.txt'
        # テストで使うファイル作成
        p1.touch()
        p2 = self.data_path / 'sample2.txt'
                # テストで使う２個目のファイルを作成
        p2.touch()
    # テスト実行対象のメソッドを定義
    def test_two_files(self):
        self.assertEqual(len(list(self.data_path.iterdir())),2)