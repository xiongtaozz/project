import cx_Oracle
conn=cx_Oracle.connect('cnooc/cnooc@10.71.197.123/orcl')

cursor=conn.cursor()
class cnooc:
    def cr(self,sql):
        a=self.sql
        sql=u"""select a.rq  日期,
            case when b.LB = 1 then '开钻(口)'
              when b.LB =2 then '完井(口)'
                when b.LB = 3 then '正钻'
                  when b.LB = 4 then '合计' end 类别,
                b.HJ  总井数合计,
                b.YT1  总井数预探井,
                b.PJ1  总井数评价井,
                b.YT2  自营井数预探井,
                b.PJ2  自营井数评价井,
                b.YT3  自营天津预探井,
                b.PJ3   自营天津评价井,
                b.YT4  自营上海预探井,
                b.PJ4   自营上海评价井,
                b.YT5  自营深圳预探井,
                b.PJ5   自营深圳评价井,
                b.YT6  自营湛江预探井,
                b.PJ6   自营湛江评价井,
                b.YT7   非自营井数预探井,
                b.PJ7  非自营井数评价井,
                b.YT8  非自营天津预探井,
                b.PJ8  非自营天津评价井,
                b.YT9  非自营上海预探井,
                b.PJ9  非自营上海评价井,
                b.YT10  非自营深圳预探井,
                b.PJ10  非自营深圳评价井,
                b.YT11  非自营湛江预探井,
                b.PJ11  非自营湛江评价井,
                b.YT12  非自营海外预探井,
                b.PJ12  非自营海外评价井 from KTYX_KT013 a,KTYX_KT013_3 b
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
