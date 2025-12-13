from unittest.mock import Mock

def test_assert_called():
    mock = Mock()
    mock.some_method()
    
    # assert_called
    mock.some_method.assert_called()
    # mock.other_method.assert_called()  # この行は失敗する


def test_assert_called_once():
    mock = Mock()
    mock.some_method()
    # assert_called_once
    mock.some_method.assert_called_once()

    # mock.some_method()
    # mock.some_method.assert_called_once() # この行は失敗する


def test_assert_called_with():
    mock = Mock()
    mock.some_method(1, 'hello', key='value')
    mock.some_method(2, 'world')

    # 最後の呼び出し（2, 'world'）を検証
    mock.some_method.assert_called_with(2, 'world')
    # mock.some_method.assert_called_with(1, 'hello', key='value') # この行は失敗する


def test_assert_called_once_with():
    mock = Mock()
    mock.some_method(100)

    mock.some_method.assert_called_once_with(100)
    # mock.some_method(200)
    # mock.some_method.assert_called_once_with(100) # この行は失敗する


def test_assert_not_called():
    mock = Mock()
    mock.some_method.assert_not_called()

    # mock.some_method()
    # mock.some_method.assert_not_called() # この行は失敗する