
class global_var:
    # case_id
    Id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'

    def get_id(self):
        """获取case_ID"""
        return global_var.Id

    def get_request_name(self):
        """获取模块名称"""
        return global_var.request_name

    def get_url(self):
        """获取url"""
        return global_var.url

    def get_run(self):
        """是否运行"""
        return global_var.run

    def get_run_way(self):
        """请求方式"""
        return global_var.request_way

    def get_header(self):
        """是否携带header"""
        return global_var.header

    def get_case_depend(self):
        """case依赖"""
        return global_var.case_depend

    def get_data_depend(self):
        """依赖的返回数据"""
        return global_var.data_depend

    def get_field_depend(self):
        """数据依赖字段"""
        return global_var.field_depend

    def get_data(self):
        """请求数据"""
        return global_var.data

    def get_expect(self):
        """获取预期结果"""
        return global_var.expect

    def get_result(self):
        """获取实际结果"""
        return global_var.result
