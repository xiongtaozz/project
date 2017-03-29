# coding:utf-8

# import pymysql
#
# conn = pymysql.connect(port=3306, host='', user='root',
#                        password='scx1123', db='testdb', charset='utf8')
# cur = conn.cursor()
# # print 'INSERT INTO STUDENT(name,number,age) VALUES(%s,%d,%d)' % ('"jack"', 15, 28)
# cur.execute('INSERT INTO STUDENT(name,number,age) VALUES(%s,%s,%s)' % ('jack', 15, 29),)
# # 增加
# conn.commit()
# # 删除
# cur.execute('DELETE STUDENT WHERE id =%s', 6)
# # 修改
# cur.execute('UPDATE STUDENT SET name=%s,number=%s WHERE id =%s', ('Jack', 16, 5))
# # print cur.fetchall()
# # 批处理
# cur.executemany('INSERT INTO STUDENT(name,number,age) VALUES(%s,%s,%s)', [('jack', 15, 29),('jack', 15, 29)])
# cur.close()
# conn.close()

na = []

def normalize(name):
    global na
    name= name.lower()
    na += list(name)
    print na
    # na[0]= na[0].upper()
    # name= ''.join(na)
    # return name
    return na

L1=['adam','LISA','barT']
map(normalize, L1)
print na
# print map(normalize, L1)
# L2=map(normalize,L1)
# print(L2)