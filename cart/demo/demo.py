# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import mechanize
import codecs
import lxml
import json
#import re
def fetch_tail(link):
	br=mechanize.Browser()
	r=br.open(link)
	html=r.read()
	soup=BeautifulSoup(html,'lxml')
	#l = soup.find('li',{'class':'dn on'})
	l=soup.body.find_all('li',class_='dn on')
	file =codecs.open('weather0.txt','w','utf-8')
	print >> file, 'date, dn,weather,temperature,wind,sunUp'
	for e in l:
		date=[]
		dn=[]
		weather=[]
		temperature=[]
		wind=[]
		sunUp=[]
		d=e.find_all('h1')
		dd=BeautifulSoup(str(d)).get_text()
		#print dd
		date.insert(0,dd)
        #
		# o=e.find_all('h2')
		# oo=BeautifulSoup(str(o)).get_text().replace("\n"," ").encode("utf-8")
		# #print oo
		# dn.append(oo)
        #
		# w=e.find_all('p',class_='wea')
		# ww=BeautifulSoup(str(w)).get_text().replace("\n"," ").encode("utf-8")
		# #print ww
		# weather.append(ww)
        #
		# t=e.find_all('p',class_='tem')
		# for r in t:
		# 	nn=BeautifulSoup(str(r.span)).get_text().replace("\n"," ").encode("utf-8")
		# 	mm=BeautifulSoup(str(r.i)).get_text().replace("\n"," ").encode("utf-8")
		# 	#print nn,mm
		# 	temperature.append(nn)
		# 	temperature.append(mm)
        #
		# wi=e.find_all('p',class_='win')
		# WI=BeautifulSoup(str(wi)).get_text().replace("\n"," ").encode("utf-8")
		# #print WI
		# wind.append(WI)
        #
		# s=e.find_all('p',class_='sunUp')
		# ss=BeautifulSoup(str(s)).get_text().replace("\n"," ").encode("utf-8")
		# #print ss
		# sunUp.append(ss)
		#print json.dumps(date, encoding='UTF-8', ensure_ascii=False)
		print >> file, '"%s","%s","%s","%s","%s","%s"' % (date,dn,weather,temperature,wind,sunUp)
		print '\t', '"%s","%s","%s","%s","%s","%s"' % (date,dn,weather,temperature,wind,sunUp)


if  __name__ == '__main__':
	url=['101070201','101010100','101120401']
	for a in url:
		link='http://www.weather.com.cn/weather1d/'+a+'.shtml '

		fetch_tail(link)