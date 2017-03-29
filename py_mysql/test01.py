# -*- coding:utf-8 -*-
import pymysql


def find(cur):

    cur.execute('SELECT id,name,number,age FROM STUDENT')  # 执行查询信息

    return cur.fetchall()


def add(cur, conn):
    cur.execute('INSERT INTO STUDENT(name,number,age) VALUES(%s,%s,%s)', ('李四', 14, 25))
    conn.commit()


def update(cur, conn):
    cur.execute('UPDATE STUDENT SET age=%s WHERE name=%s', ('28', '李四'))
    conn.commit()


conn = pymysql.connect(host='', port=3306, user='root', passwd='scx1123',
                       db='testdb', charset='utf8')  # 连接数据库

cur = conn.cursor()  # 创建游标

# # 执行查询操作
print find(cur)

# 执行插入操作
# add(cur, conn)

# 更改操作
update(cur, conn)

cur.close()
conn.close()


