# coding:utf-8
from mysql_class import pyCls


class pyOther(pyCls):

    # def __init__(self,db,password):
    #     super(pyOther, self).__init__()
    def add(self, sql, item):
        self.cur.execute(sql, item)
        self.conn.commit()


if __name__ == '__main__':
    pyOther(db='testdb', password='scx1123').add\
        ('INSERT INTO STUDENT(name,number,age) VALUES(%s,%s,%s)', ('王五', 20, 30))

