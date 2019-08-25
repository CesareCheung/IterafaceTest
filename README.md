1、**runmethod.py**：请求方式方法封装，_`verify=False`_ 当请求为https时关闭SSL安全验证，`requests.packages.urllib3.disable_warnings()`  运行程序时去掉提示安全提示信息

2、**test_method.py**：测试程序，unittest运用

3、**data_config.py**：获取excel文件常量方法封装

4、**dependent_data.py**：解决数据依赖问题，如下个接口需要用到上个接口的返回值

5、**get_data.py**：获取excel中的数据

6、**run_test.py**：主运行程序

7、**common_util.py**：判断一个字符串是否在另一个字符串中，用于断言

8、**operation_excel.py**：操作excel方法封装

9、**operation_json.py**：操作JSON文件

10、**send_email.py**：以邮件方式发送测试报告方法封装

11、**case**：用例

12、**data.json**：请求数据
