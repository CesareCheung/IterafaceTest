import unittest


class TestMethod(unittest.TestCase):
    # 每次方法之前执行
    def setUp(self):
        print('test--->>>setUp')

    # 每次方法后执行
    def tearDown(self):
        print('test--->>>tearDown')

    def test_01(self):
        print('这个是测试方法！')
