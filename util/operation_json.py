import json


class OperationJson:
    """操作json文件"""

    def __init__(self):
        self.data = self.read_data()

    def read_data(self, file_name='../dataconfig/data.json'):
        """
        读取json文件
        :param file_name:文件路径
        :return:
        """
        with open(file_name) as fp:
            data = json.load(fp)
        return data

    def get_data(self, key):
        """根据关键字获取对应数据"""
        return self.data[key]


if __name__ == '__main__':
    # file_path = "../dataconfig/data.json"
    opejson = OperationJson()
    print(opejson.read_data())
    print(opejson.get_data('addcar'))
