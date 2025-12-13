import unittest
from unittest.mock import patch
from my_module import get_data

class MyTest(unittest.TestCase):
    @patch('my_module.requests.get')
    def test_get_data_success(self, mock_get):
        # モックの戻り値を設定
        mock_get.return_value.status_code = 200

        # テスト対象の関数を実行
        result = get_data()

        # 結果とモックの呼び出しを検証
        self.assertEqual(result, 200)
        mock_get.assert_called_once()

'''
@patch('my_module.requests.get')は、my_module内でrequests.getが呼び出された際に、
その呼び出しをMagicMockオブジェクトに置き換える
そのモックが引数mock_getとしてテストメソッドに渡される
'''

class MyTest2(unittest.TestCase):
    def test_get_data_with_context_manager(self):
        # withブロック内でのみrequests.getをモック化
        with patch('my_module.requests.get') as mock_get:
            # モックの戻り値を設定
            mock_get.return_value.status_code = 200

            # テスト対象の関数を実行
            result = get_data()

            # 結果とモックの呼び出しを検証
            self.assertEqual(result, 200)
            mock_get.assert_called_once()
        
        # withブロックを抜けると、requests.getは元の振る舞いに戻る