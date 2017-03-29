# coding:utf-8
from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse
from django.utils.translation import ugettext as _  # django 工具类,为了简化程序代码
import gettext  # 内置
import time


def test1_view(request):
    # 获得系统本地时间，返回的格式是 UTC 中的 struct_time 数据
    t = time.localtime()
    # 第 6 个元素是 tm_wday , 范围为 [0,6], 星期一 is 0
    n = t[6]
    # 星期一到星期日字符串
    # weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekdays = [_('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'), _('Friday'), _('Saturday'), _('Sunday')]
    # 返回一个 HttpResponse、，这段代码将用来返回服务器系统上是星期几。
    return HttpResponse(weekdays[n])


# def test1_view(request):
#     # 获得系统本地时间，返回的格式是 UTC 中的 struct_time 数据
#     t = time.localtime()
#     # 第 6 个元素是 tm_wday , 范围为 [0,6], 星期一 is 0
#     n = t[6]
#     # 星期一到星期日字符串
#     weekdays = [_('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'), _('Friday'), _('Saturday'), _('Sunday')]
#     # 返回一个 HttpResponse、，这段代码将用来返回服务器系统上是星期几。
#     return HttpResponse(weekdays[n])
#
#
def test2_view(request):
    code = _("The second sentence is from the Python code.")
    return render_to_response('i18n_index.html', locals())


