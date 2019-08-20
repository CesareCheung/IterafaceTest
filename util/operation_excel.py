import xlrd
from xlutils.copy import copy


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
            self.file_name = '../dataconfig/case1.xls'
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

    def get_cell_value(self, row, col):
        """获取单元格的内容"""
        return self.data.cell_value(row, col)

    def write_value(self, row, col, value):
        """
        回写数据到excel
        :param row:行
        :param col:列
        :param value:返回值
        :return:
        """
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    def get_row_data(self,case_id):
        """
        根据对应的case_id获取对应行的内容
        :param case_id:测试用例ID
        :return:
        """
        row_num=self.get_row_num(case_id)  #根据对应的case_id拿到对应的行号
        row_data=self.get_row_value(row_num)
        return row_data


    def get_row_num(self,case_id):
        """
        根据对应的case_id找到对应的行号
        :param case_id:
        :return:
        """
        num=0
        cols_data=self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num+=1


    def get_row_value(self,row):
        """
        根据行号，找到该行的内容
        :param row:行号
        :return:
        """
        tables=self.data
        row_data=tables.row_values(row)
        return row_data

    def get_cols_data(self,col_id):
        """
        获取某一列的内容
        :param col_id:列号
        :return:
        """
        if col_id !=None:
            cols=self.data.col_values(col_id)
        else:
            cols=self.data.col_values(0)
        return cols


if __name__ == '__main__':
    opera = OperationExcel()
    opera.get_data()
    print(opera.get_data().nrows)
    print(opera.get_lines())
    print(opera.get_cell_value(1, 2))
