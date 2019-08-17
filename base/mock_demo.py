from unittest import mock


def mock_test(mock_method, request_data, url, method, response_data):
    """模拟mock 封装"""
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return res
