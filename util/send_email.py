import smtplib
from email.mime.text import MIMEText


class SendEmail:
    """邮件方式发送报告"""
    global send_user
    global email_host
    global password
    send_user = "xxxx@163.com"
    email_host = "smtp.163.com"
    password = 'xxxxxx'

    def send_mail(self, user_list, sub, content):
        """
        发送邮件
        :param user_list: 收件人列表
        :param sub: 主题
        :param content: 内容
        :return:
        """
        user = "xxxx.com" + "<" + send_user + ">"
        message = MIMEText(content, _subtype="plain", _charset="utf-8")
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()


if __name__ == '__main__':
    send = SendEmail()
    user_list = ['1689719986@qq.com']
    sub = '测试主题'
    content = "测试"
    send.send_mail(user_list, sub, content)
