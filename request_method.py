import requests
import json


class RunMain:

    def __init__(self, url, method, data=None):
        self.res = self.run_method(url, method, data)


    def send_get(self, url, data):
        """
        发送get请求
        :param url:请求地址
        :param method:类型(GET)
        :param data: 参数
        :return:
        """
        res = requests.get(url, data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def send_post(self, url, data):
        """
        发送post请求
        :param url:请求地址
        :param method:类型(POST)
        :param data: 参数
        :return:
        """
        res = None
        res = requests.post(url, data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def run_method(self, url, method, data=None):
        """
        判断请求类型，并进行对应请求调用
        :param url:
        :param method:
        :param data:
        :return:
        """
        if method == "GET":
            res = self.send_get(url, data)
        elif method == "POST":
            res = self.send_post(url, data)
        else:
            print("暂未封装该接口类型！")
        return res


if __name__ == '__main__':
    url = "http://httpbin.org/get"
    data = {
        "username": "测试",
        "model_id": "12"
    }

    run = RunMain(url, "GET", data)

    print(run.res)
