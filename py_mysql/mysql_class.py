# coding:utf-8

import pymysql


class pyCls(object):
    def __init__(self, port=3306, host='', user='root', password='', db='', charset='utf8'):
        self.conn = pymysql.connect(port=port, host=host, user=user,
                                    password=password, db=db, charset=charset)
        self.cur = self.conn.cursor()
        print u'连接池打开'

    def add(self, sql, item):
        ''' self.cur.execute(sql, item)
        self.conn.commit() '''
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def addall(self):
        pass

    def __del__(self):
        print u'连接池关闭'
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    pyCls(db='testdb', password='scx1123')