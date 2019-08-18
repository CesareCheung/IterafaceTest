from util.operation_excel import OperationExcel
from data import data_config
from util.operation_json import OperationJson


class GetData:

    def __init__(self):
        self.opera_excel = OperationExcel()
        self.opera_json = OperationJson()

    def get_case_lines(self):
        """获取excel行数，即case的个数"""
        return self.opera_excel.get_lines()

    def get_is_run(self, row):
        """获取是否执行"""
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def is_header(self, row):
        """
        是否携带header
        :param row: 行号
        :return:
        """
        col = data_config.get_header()
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    def get_request_method(self, row):
        """
        获取请求方式
        :param row: 行号
        :return:
        """
        # col 列
        col = data_config.get_run_way()
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    def get_request_url(self, row):
        """
        获取url
        :param row: 行号
        :return:
        """
        col = data_config.get_url()
        url = self.opera_excel.get_cell_value(row, col)
        return url

    def get_request_data(self, row):
        """
        获取请求数据
        :param row:行号
        :return:
        """
        col = data_config.get_data()
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        else:
            return data

    def get_data_for_json(self, row):
        """
        通过关键字拿到data数据
        :param row:
        :return:
        """
        request_data = self.opera_json.get_data(self.get_request_data(row))
        return request_data

    def get_expcet_data(self, row):
        """
        获取预期结果
        :param row:
        :return:
        """
        col = data_config.get_expect()
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == "":
            return None
        else:
            return expect
