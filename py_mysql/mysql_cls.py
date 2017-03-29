# -*- coding:utf-8 -*-
import pymysql
import json

# json.loads() -->字典


class MysqlCls(object):

    def __init__(self, host='', port=3306, user='root', passwd=None, db=None, charset='utf8'):
        self.__conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        self.__cur = self.__conn.cursor()

    def add_update_sql(self, sql, item):
        self.__cur.execute(sql, item)
        self.__conn.commit()

    def delete_sql(self, sql, item):
        self.__cur.execute(sql, item)

    def find_sql(self, sql,):
        pass

    def add_many_sql(self, sql, items):
        self.__cur.executemany(sql, items)
        self.__conn.commit()

    def __del__(self):
        self.__cur.close()
        self.__conn.close()

if __name__ == '__main__':
    mysql = MysqlCls(passwd='scx1123', db='testdb')
    # mysql.add_update_sql('INSERT INTO STUDENT(name,number,age) VALUES(%s,%s,%s)', ('李五', 16, 25))
    mysql.add_many_sql('INSERT INTO STUDENT(name,number,age) VALUES(%s,%s,%s)', [('李六', 19, 27), ('李七', 20, 26)])
    # mysql.add_sql('UPDATE STUDENT set number=%s WHERE name=%s', (20, '李五'))
    # 'SELECT * FROM STUDENT WHERE age >%s and name like "王%" and number > %s'
    # 'a' + 'b'
    # sql = 'SELECT * FROM STUDENT WHERE'
    # t = {'name': '王', 'age':20}
    # for x in t.keys():
    #     if x == 'name':
    #         sql += ' name like %s' % t[x] + '%'
    #         print sql
    #     if x == 'age':
    #         sql += ' name like %s' % t[x] + '%'
    #         print sql