from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse
import json


class DependentData:

    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()

    def get_case_line_data(self):
        """
        通过case_id去获取该case_id的整行数据
        :param case_id: 用例ID
        :return:
        """
        rows_data = self.opera_excel.get_row_data(self.case_id)
        return rows_data

    def run_dependent(self):
        """
        执行依赖测试，获取结果
        :return:
        """
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data, header)
        return json.loads(res)

    def get_data_for_key(self, row):
        """
        根据依赖的key去获取执行依赖case的响应然后返回
        :return:
        """
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]
