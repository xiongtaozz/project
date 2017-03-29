#coding:utf-8
import urllib
import urllib2
import re
url = 'http://www.maiziedu.com/user/login/'
values = {'username':'qlp001@qq.com','password':'123123123'}
data = urllib.urlencode(values)
request =urllib2.Request(url,data)
response =urllib2.urlopen(request)
# print response.read()
response = urllib2.urlopen('http://www.maiziedu.com/course/teachers/?page=1')
html = response.read()
# print html
#用正则匹配需要的数据
#<a href="/course/python/425-5465/" lesson_id="5465">1.&nbsp;课程介绍</a>
#<a href="/[a-z]{0,10}/[a-z]{0,10}/[0-9]{4}-[0-9]{5}/" lesson_id="[0-9]{10}"></a>
'''
 <div class="teacherListR">
    <p class="font20 color00 marginB14 t3out p">Merin<a href="/group/common/course/70885/" class="go font12">查看他的课程</a></p>
    <p class="color66 marginB14"><span class="color99">职位：</span></p>
    <p class="color66"><span class="color99">简介：</span>长期致力于PHP内核，扩展研究。熟悉Linux,Mysql,Memcached, Redis,Mongo等开源产品，曾就任于北京某大型互联网公司，北京某大型游戏公司，担任过开发工程师，项目经理，主管。</p>
 </div>
'''
recmp = '<div class="teacherListR">[\s|\S]*?<p class="font20 color00 marginB14 t3out p">(.*)<a href="/[a-z]{0,}/[a-z]{0,}/[a-z]{0,}/[0-9]{0,}/" class="go font12">.*</a></p>[\s|\S]*?<p class="color66 marginB14"><span class="color99">.*</span></p>[\s|\S]*?<p class="color66"><span class="color99">.*</span>(.*)</p>[\s|\S]*?</div>'
list_a = re.compile(recmp)
thislist = list_a.findall(html)
print len(thislist)
for li in thislist:
    print li[0],li[1]