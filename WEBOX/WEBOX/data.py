#coding:utf-8
from django.utils import timezone
from we30.models import *
from we30c.models import *
from we30p.models import *
import xlrd


data = xlrd.open_workbook('model.xlsx')
table = data.sheets()[0]

nrows = table.nrows



for i in range(nrows):
    we30c = we30c_4th(type=table.row_values(i)[0],order_number=table.row_values(i)[1],name=table.row_values(i)[2],
                      SN=table.row_values(i)[3],MAC=table.row_values(i)[4],question=table.row_values(i)[5],
                      phenomenon=table.row_values(i)[6],question_type=table.row_values(i)[7],reason=table.row_values(i)[8],
                      ranges=table.row_values(i)[9],pub_date=timezone.now())
    we30c.save()

# we30c = we30c_1st(type='保修',order_number='1111111111',name='李四',SN='we30c092500011',MAC='BD14CA123D31',
#                    question='不开机',phenomenon='不开机',question_type='硬件',reason='rk3368',ranges='RK芯片问题',
#                    pub_date=timezone.now())

# we30 = we30_1st(type='保修',order_number='1111111111',name='张三',SN='we30092500011',MAC='00:25:69:57:12:51',
#                    question='不开机',phenomenon='不开机',question_type='硬件',reason='rk3368',ranges='RK芯片问题',
#                    pub_date=timezone.now())
#
#
# we30.save()
#
#
# we30 = we30_2nd(type='保修',order_number='1111111111',name='张三1',SN='we30092500011',MAC='00:25:69:57:12:51',
#                    question='不开机',phenomenon='不开机',question_type='硬件',reason='rk3368',ranges='RK芯片问题',
#                    pub_date=timezone.now())








# we30c.save()
# we30c_1st.objects.all()

# we30p = we30p_1st(type='保修',order_number='1111111111',name='王无',SN='we30p092500011',MAC='00:25:69:57:12:51',
#                    question='不开机',phenomenon='不开机',question_type='硬件',reason='rk3368',ranges='RK芯片问题',
#                    pub_date=timezone.now())
#
#
# we30p.save()
# we30p_1st.objects.all()
