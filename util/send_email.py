import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail:
    """邮件方式发送报告"""
    global send_user
    global email_host
    global password
    send_user = "XXX@163.com"
    email_host = "smtp.163.com"
    password = 'XXX'

    def send_mail(self, user_list, sub, content):
        """
        发送邮件
        :param user_list: 收件人列表
        :param sub: 主题
        :param content: 内容
        :return:
        """
        user = "XXX@163.com" + "<" + send_user + ">"
        message = MIMEMultipart()
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ",".join(user_list)
        body = MIMEText(content, _subtype="plain", _charset="utf-8")  # 邮件内容
        message.attach(body)
        # 添加附件
        att = MIMEText(open("../dataconfig/case1.xls", "rb").read(), "base64",
                       "utf-8")  # 打开附件地址
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="case1.xls"'
        message.attach(att)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        """
        发送报告
        :param pass_list:
        :param fail_list:
        :return:
        """
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        user_list = ['hhhh@qq.com','aaaa@qq.com']

        sub = '接口自动化测试报告'
        content = f"此次接口测试一共运行用例为：{count_num}，通过个数为：{pass_num}，失败个数为：{fail_num}，通过率为：{pass_result},报告详情请查看附件！"
        self.send_mail(user_list, sub, content)


if __name__ == '__main__':
    send = SendEmail()
    send.send_main([1, 2, 3, 4], [6, 2])
