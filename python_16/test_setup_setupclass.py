import unittest

class MyTest(unittest.TestCase):
    # テストメソッドが実行される直前に呼び出される
    def setUp(self):
        print("setUp called: Setting up a new object for a test...")
        self.my_object = {"key": "value"}

    def test_method_1(self):
        print("Running test_method_1...")
        self.assertEqual(self.my_object["key"], "value")

    def test_method_2(self):
        print("Running test_method_2...")
        self.assertIn("key", self.my_object)

class MyTest2(unittest.TestCase):
    # すべてのテストメソッドが実行される前に実行
    @classmethod
    def setUpClass(cls):
        print("setUpClass called: Setting up shared resources for all tests...")
        cls.shared_resource = "This is a shared resource."

    def test_method_1(self):
        print("Running test_method_1...")
        self.assertEqual(self.shared_resource, "This is a shared resource.")

    def test_method_2(self):
        print("Running test_method_2...")
        self.assertIn("shared", self.shared_resource)