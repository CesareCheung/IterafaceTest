import xlrd


# data = xlrd.open_workbook("../dataconfig/interface.xlsx")
# tables = data.sheets()[0]
# print(tables.nrows)  # 获取总行数
# print(tables.cell_value(2, 4))  # 获取第二行第四列的值


class OperationExcel:
    """操作Excel"""

    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/interface.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    def get_data(self):
        """
        获取sheets的内容
        :param file_name:文件路径
        :param sheet_id:
        :return:
        """
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        """获取单元格行数"""
        tables = self.data
        return tables.nrows

    def get_cell_value(self,row,col):
        """获取单元格的内容"""
        return self.data.cell_value(row,col)


if __name__ == '__main__':
    opera = OperationExcel()
    opera.get_data()
    print(opera.get_data().nrows)
    print(opera.get_lines())
    print(opera.get_cell_value(1,2))
