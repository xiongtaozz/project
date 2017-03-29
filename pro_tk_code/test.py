# coding:utf-8
import sys
import re

# # ascii --->unicode
# print sys.getdefaultencoding()
#
# # 输入类容
# str = raw_input('>')
# print str
# html ='''
# <div class="threadlist_lz clearfix">
#                 <div class="threadlist_title pull_left j_th_tit
# ">
#
#
#     <a class="j_th_tit " target="_blank" title="如何从零开始学python？" href="/p/4606205714">如何从零开始学python？</a>
# </div><div class="threadlist_author pull_right">
#     <span data-field="{&quot;user_id&quot;:625543823}" title="主题作者: 杨兵507" class="tb_icon_author "><i class="icon_author"></i><a target="_blank" href="/home/main/?un=%E6%9D%A8%E5%85%B5507&amp;ie=utf-8&amp;fr=frs" class="frs-author-name j_user_card " data-field="{&quot;un&quot;:&quot;\u6768\u5175507&quot;}">杨兵507</a><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
#     <span title="创建时间" class="pull-right is_show_create_time">6-12</span>
# </div>
#             </div>
# '''
# patten = re.compile('<div class="threadlist_lz.*?">.*?<a class="j_th_tit.*?"*.?title="(.*?)"'
#                     ' href="(.*?)">.*?<span.*?;}">(.*?)<', re.S)
# con = re.findall(patten, html)
# print con[0][0].decode('utf-8')
# print con[0][1]
# print con[0][2].decode('utf-8')

'''
项目制作
项目描述
写一个函数，该函数能判断传入的参数是否是一个完数，如果是完数则返回True，否则返回False
提示：完数就是一个数等于他的因子之和，如6=1+2+3; 那么这个数就是完数。
分子数:1-5
什么因子数:6%(1-5) == 0 说明是 6的因子数
1, 得到分子数
2, 通过分子数得到因子数
3, 因子相加如果等于6 则是完数

'''

a = raw_input(u'请输入数字>')

# print [x for x in range(1,int(a)) if int(a)%x==0]
# print sum([x for x in range(1,int(a)) if int(a)%x==0])
if int(a) == sum([x for x in range(1, int(a)) if int(a) % x == 0]):
    print '%r 是完数'.decode('utf-8') % a
else:
    print '%r 不是完数'.decode('utf-8') % a

# '6'
# def index(a):
#     sumer = 0
#     # 1
#     for x in range(1, a):  # 分子数
#         # 2
#         if a % x == 0:
#             sumer += x
#     if sumer == a:
#         print '%d 是完数'.decode('utf-8')% a
#     else:
#         print '%d 不是完数'.decode('utf-8')% a
#
# index(int(a))

# %s 字符串
# %d 数字
# %r 所有
