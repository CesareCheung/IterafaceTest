class CommonUtil:
    def is_contain(self, str_one, str_two):
        """
        判断一个字符串是否在另一个字符串中
        :param str_one:查找的字符串
        :param str_two:被查找的字符串
        :return:
        """
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
