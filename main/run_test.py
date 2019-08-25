from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.send_email import SendEmail


class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()

    def go_on_run(self):
        """程序执行"""
        pass_count = []
        fail_count = []
        res = None
        # 获取用例数
        rows_count = self.data.get_case_lines()
        # 第一行索引为0
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)

                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    # 更新请求字段
                    request_data[depend_key] = depend_response_data
                res = self.run_method.run_main(method, url, request_data)
                # print(res)
                # print(request_data)
                # return res
                # print(res)
                if self.com_util.is_contain(expect, res):
                    self.data.write_result(i, "Pass")
                    pass_count.append(i)
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
        # 发送邮件
        # self.send_email.send_main(pass_count, fail_count)

        print(f"通过用例数：{len(pass_count)}")
        print(f"失败用例数：{len(fail_count)}")


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
