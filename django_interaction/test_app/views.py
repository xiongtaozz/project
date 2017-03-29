# coding:utf-8
from django.shortcuts import render,HttpResponse
from django.utils.translation import ugettext as _
import time
# Create your views here.


def test1_view(request):
    # 获得系统本地时间，返回的格式是 UTC 中的 struct_time 数据
    t = time.localtime()
    # 第 6 个元素是 tm_wday , 范围为 [0,6], 星期一 is 0
    n = t[6]
    # 星期一到星期日字符串
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']
    # weekdays = [_('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'), _('Friday'),
    #             _('Saturday'), _('Sunday')]
    # 返回一个 HttpResponse、，这段代码将用来返回服务器系统上是星期几。
    return HttpResponse(weekdays[n])