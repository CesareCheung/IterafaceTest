import json
import unittest
# from base.HTMLTestRunner import HTMLTestRunner
from base.HTMLTestRunnerCN import HTMLTestRunner
import HTMLReport

from base.demo import RunMain


class TestMethod(unittest.TestCase):
    """测试"""

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
        res = self.run.run_method(url, "POST", data)
        res = json.loads(res)
        print(res)
        print("第一个case")
        self.assertEqual(res['errorCode'], 1007, '测试失败')

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
    suite = unittest.TestSuite()
    suite.addTest(TestMethod("test_01"))
    suite.addTest(TestMethod("test_02"))
    fithpath = '../report/result.html'
    with open(fithpath, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='测试报告的标题:',
            description='测试报告的描述:这是两个测试用例')
        runner.run(suite)


    # HTMLReport.TestRunner(
    #     report_file_name="test",
    #     title='接口自动化',
    #     description='ERP项目',
    #     thread_count=1
    # ).run(suite)
