import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        # 各テストの前に、一時的なファイルを作成
        self.file = open("temp_file.txt", "w+")
        self.file.write("test data")

    def tearDown(self):
        # 各テストの後に、一時ファイルを閉じて削除
        self.file.close()
        import os
        os.remove("temp_file.txt")
        print("tearDown: temp_file.txt removed.")
        print('-'*30)

    def test_file_content(self):
        # ファイルの内容をテストする
        self.file.seek(0)
        content = self.file.read()
        self.assertEqual(content, "test data")
        print("test_file_content completed.")

class MyTest2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 全テストの前に、データベース接続を確立
        print("setUpClass: Establishing shared database connection...")
        cls.db_connection = "db_connection_object"

    @classmethod
    def tearDownClass(cls):
        # 全テストの後に、データベース接続を閉じる
        print("tearDownClass: Closing shared database connection.")
        cls.db_connection = None

    def test_db_query_1(self):
        # 共有リソースを使ってテストを実行
        self.assertIsNotNone(self.db_connection)

    def test_db_query_2(self):
        self.assertIsInstance(self.db_connection, str)

