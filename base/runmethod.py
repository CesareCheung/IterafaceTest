import requests


class RunMethod:

    def post_main(self, url, data, header=None):
        """
        post请求方式
        :param url:请求地址
        :param data:请求数据
        :param header:请求头部
        :return:
        """
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data=None, header=None):
        """
        get请求方式
        :param url:请求地址
        :param data:请求数据
        :param header:请求头部
        :return:
        """
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        """
        运行函数
        :param method:请求方式
        :param url:请求地址
        :param data:请求数据
        :param header:请求头部
        :return:
        """
        res = None
        if method == "post":
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return res
