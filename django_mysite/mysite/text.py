import cx_Oracle
conn=cx_Oracle.connect('cnooc/cnooc@10.71.197.123/orcl')

cursor=conn.cursor()
class cnooc:
    def cr(self,sql):
        a=self.sql
        sql=u"""select a.rq  ����,
            case when b.LB = 1 then '����(��)'
              when b.LB =2 then '�꾮(��)'
                when b.LB = 3 then '����'
                  when b.LB = 4 then '�ϼ�' end ���,
                b.HJ  �ܾ����ϼ�,
                b.YT1  �ܾ���Ԥ̽��,
                b.PJ1  �ܾ������۾�,
                b.YT2  ��Ӫ����Ԥ̽��,
                b.PJ2  ��Ӫ�������۾�,
                b.YT3  ��Ӫ���Ԥ̽��,
                b.PJ3   ��Ӫ������۾�,
                b.YT4  ��Ӫ�Ϻ�Ԥ̽��,
                b.PJ4   ��Ӫ�Ϻ����۾�,
                b.YT5  ��Ӫ����Ԥ̽��,
                b.PJ5   ��Ӫ�������۾�,
                b.YT6  ��Ӫտ��Ԥ̽��,
                b.PJ6   ��Ӫտ�����۾�,
                b.YT7   ����Ӫ����Ԥ̽��,
                b.PJ7  ����Ӫ�������۾�,
                b.YT8  ����Ӫ���Ԥ̽��,
                b.PJ8  ����Ӫ������۾�,
                b.YT9  ����Ӫ�Ϻ�Ԥ̽��,
                b.PJ9  ����Ӫ�Ϻ����۾�,
                b.YT10  ����Ӫ����Ԥ̽��,
                b.PJ10  ����Ӫ�������۾�,
                b.YT11  ����Ӫտ��Ԥ̽��,
                b.PJ11  ����Ӫտ�����۾�,
                b.YT12  ����Ӫ����Ԥ̽��,
                b.PJ12  ����Ӫ�������۾� from KTYX_KT013 a,KTYX_KT013_3 b
                where a.guid = b.guid and b.guid <> '3568CAE4-C488-477A-B0C1-F9EE55C2F828' order by a.rq,b.lb"""
        try:
            cursor.execute(sql)
            rows=cursor.fetchall()
            for row in rows:
                print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %(row[0],row[1],row[2],row[3],\
                                                      row[4],row[5],row[6],row[7],\
                                                      row[8],row[9],row[10],row[11],\
                                                      row[12],row[13],row[14],row[15],\
                                                      row[16],row[17],row[18],row[19],\
                                                      row[20],row[21],row[22],row[23],\
                                                      row[24],row[25],row[26])
            print "this:",cursor.rowcount
        except:
            print "this is an error"
            cursor.close()
            conn.close()
        return

cursor.close()
conn.close()
