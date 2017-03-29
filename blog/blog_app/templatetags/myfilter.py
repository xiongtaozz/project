# -*- coding:utf-8 -*-
from django import template
import time, datetime
register = template.Library()


@register.filter
def date_time(key_time):
    start_time = datetime.datetime.now()
    end_time = str_time(key_time)
    z_time = start_time - end_time
    d_time = (z_time.seconds/60)/60
    print z_time
    print d_time
    if z_time.days == 0:
        if d_time >= 1 and d_time <= 24:
            r_time = "%s 小时之前".decode('utf-8')% str(d_time)
        elif d_time == 0:
            if z_time.seconds/60 < 5:
                r_time = "刚刚".decode('utf-8')
            else:
                r_time = "%s 分钟之前".decode('utf-8')% str(z_time.seconds/60)
        elif d_time > 24:
            r_time = "%s 天之前".decode('utf-8')% str(d_time/60)
        # elif d_time > 720:
        #     return "%s 月之前".decode('utf-8')% str((d_time/60)/30)
    else:
        if z_time.days > 365:
            r_time = "%s 年之前".decode('utf-8')% str(z_time.days/365)
        elif d_time == 0:
            r_time = "%s 天之前".decode('utf-8')% str(z_time.days if z_time.days else 1)
        else:
            r_time = "%s 月之前".decode('utf-8')% str(z_time.days/30 if z_time.days/30>1 else 1)

    return r_time


def str_time(d):
    t = time.strptime(d,"%Y-%m-%d %H:%M:%S")  # struct_time类型
    d = datetime.datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)  # d atetime类型
    return d

# register.filter('date_time', date_time)
# print date_time('2017-3-27 15:46:00')
