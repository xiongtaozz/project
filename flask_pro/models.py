# -*- coding:utf-8 -*-
import pymysql

# conn = pymysql.connect(host='', port=3306, user='root', passwd='scx1123', db='testdb')
# cur = conn.cursor()
#
# '实现业务'
# # cur.execute()
# findall()
# cur.close()
# conn.close()


class Pool(object):

    def __init__(self):
        self.conn = pymysql.connect(host='', port=3306, user='root', passwd='scx1123', db='testdb')
        self.cur = self.conn.cursor()

    # 查询所有Product类容
    def findsql(self):
        self.cur.execute('SELECT * FROM PRODUCT')
        restul = self.cur.fetchall()
        if restul:
            for rec in restul:
                print rec[0], rec[1]
        return

    def __del__(self):
        # super(Pool, self).__del__()
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    pool = Pool()
    pool.findsql()



