from unittest.mock import Mock, MagicMock

def test_mock_method():
    # mockインスタンス生成
    mock_object = Mock()

    # 関数の返す値を設定
    mock_object.my_method.return_value = "Mocked result"

    # 実行した結果（Mocked result）が入る
    result = mock_object.my_method(1, 2)

    # 結果が正しいか比較
    assert result == "Mocked result"

    # 呼ばれた回数が1回か確認
    mock_object.my_method.assert_called_once_with(1, 2)


def test_magic_mock_method():
    # MagicMockオブジェクトを作成
    magic_mock = MagicMock()

    # マジックメソッドの振る舞いを設定
    magic_mock.__len__.return_value = 10
    magic_mock.__getitem__.return_value = "item"

    print(len(magic_mock)) # 10
    print(magic_mock[0])   # "item"

    # マジックメソッドの呼び出し履歴も検証可能
    magic_mock.__len__.assert_called_once()
    magic_mock.__getitem__.assert_called_with(0)
