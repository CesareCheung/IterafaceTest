import pymysql.cursors
import json


class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host='11111',
            port=3306,
            user='1111',
            passwd='111',
            db='111',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result
    # 更新SQL
    def update_one(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("SELECT * from odi_order WHERE order_no='1111'")
    print(res)
