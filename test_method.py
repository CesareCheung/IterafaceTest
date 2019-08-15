import json
import unittest

from demo import RunMain


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()


    def tearDown(self):
        print('test--->>>tearDown')

    def test_01(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': 1001
        }
        res=self.run.run_method(url,"POST",data)
        res=json.loads(res)
        print(res)
        print("第一个case")
        self.assertEqual(res['errorCode'],1007,'测试失败')
    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0'
        }

        res = json.loads(self.run.run_method(url, 'POST', data))
        self.assertEqual(res['errorCode'], 1007, "测试失败")
        print(res)
        print("第二个case")


if __name__ == '__main__':
    # unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(TestMethod("test_02"))
    unittest.TestRunner().run(suite)
