import json


class OperationJson:
    """操作json文件"""

    def get_json(self, file_name):
        """
        获取json数据
        :param file_name:文件路径
        :return:
        """
        with open(file_name) as fp:
            data = json.load(fp)
        return data


if __name__ == '__main__':
    file_path = "../dataconfig/data.json"
    operta = OperationJson()
    print(operta.get_json(file_path)['user'])

