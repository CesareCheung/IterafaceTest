from dingtalkchatbot.chatbot import DingtalkChatbot


class SendText:
    def __init__(self, webhook):
        # 初始化机器人小丁
        self.xiaoding = DingtalkChatbot(webhook)

    def send(self):
        # Text消息@所有人
        self.xiaoding.send_text(msg='我是打包机器人！', is_at_all=False)

        self.xiaoding.send_link(title='苹果打包地址', text='测试环境', message_url='https://www.com')
        self.xiaoding.send_link(title='安卓打包地址', text='测试环境', message_url='https://www..com')


if __name__ == '__main__':
    # WebHook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token='
    send_text = SendText(webhook)
    send_text.send()
