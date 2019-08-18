import requests
import json


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    data = {
        'cart': '11'
    }
    run = RunMethod()
    run_test = run.run_main(method="GET", url=url, data=data)
    print(run_test)
