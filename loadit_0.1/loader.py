import sys, time, os, re, cookielib, mechanize
#import urllib, urllib2, re
from glob import glob
from mechanize import urlopen, ParseResponse
# http://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup, SoupStrainer, UnicodeDammit
from utils import *

# Create a browser and a cookiejar
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()

#For filling the score forms
# GRS_URL =  'http://202.118.83.94:85/'
USERNAME = '20051084'
PASSWORD = '20051084'
ROLE = '2' # as a teacher

"""
Base class for loader variants
"""

class Loader():
	def login(self, url='', usrname=USERNAME, passwd=PASSWORD, debug='info'):
		pass

	def query_by_form(self, url='', ddlYear=None, ddlTerm=None, debug='info'):
		pass

	def load_scores(self, txtExamTime=None, rblTag=None, debug='info'):
		pass

class GRSLoader():
	def __init__(self, app=None):
		self.app = app

	def course_in(self, td_tag='<td></td>', debug='info'):
		strtd = td_tag.__str__()
		if debug=='debug' or debug=='verbose':
			print '[DEBUG]', strtd,
		strtd = strtd.replace('\r', ' ')
		strtd = strtd.replace('\n', ' ')
		strtd = re.search('(?<=>)\S+', strtd).group(0)
		if '<' in strtd:
			m = re.search('\S+(?=</td>)', strtd)
			if m != None:
				strtd = m.group(0)
		if debug=='debug' or debug=='verbose':
			print strtd
		return strtd

	def read_scores(self, scoresin):
		return read_scores(self.app.task, scoresin)

	def login(self, url='login.aspx', usrname=USERNAME, passwd=PASSWORD, role=ROLE, debug='info'):
		print '[INFO ] login start ...'
		#Set cookies
		br.set_cookiejar(cj) 
		br.set_handle_equiv(True)
		# comment next line because it cases coding problem with br.response
		# br.set_handle_gzip(True)
		br.set_handle_redirect(True)
		br.set_handle_referer(True)
		br.set_handle_robots(False)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.11) Gecko/20100701 Firefox/3.5.11')]
		
		if debug=='debug' or debug=='verbose':
			br.set_debug_http(True)
			br.set_debug_responses(True)

		# Open the login page
		br.open(self.app.task['baseurl']+url)
		br.select_form(nr = 0)          # Find the login form by index
		br.set_all_readonly(False)
		br.form['txtID'] = usrname 
		br.form['txtPwd'] = passwd 
		br.form['hftypes'] = role
		# Submit the form to sign in
		br.submit()
		self.app.task['stage'] = 'login'

		if debug=='verbose':
			print br.response().read() 

	""" 
	query the score form by using mechanize purely
	(PROBLEM) - failed to get the student list
	FIX IT! The problem is caused by the enabled btnSearch. In fixing it, I also encountered the problematic encoding of br.response(), which is cause by br.set_handle_gzip(True)
	http://202.118.83.94:85/Teacher/ScoreInput.aspx?m=webm_Tea_Maintinfo_scorein
	http://www.blooberry.com/indexdot/html/topics/urlencoding.htm
	https://docs.python.org/2/library/re.html
	"""
	def query_by_form(self, url='Teacher/ScoreInput.aspx?m=webm_Tea_Maintinfo_scorein', ddlYear='2015-2016', ddlTerm='1', debug='info'):
		print '[INFO ] query_by_form start ...'
		# The passed login_grs actually gives us links to the score form
		br.open(self.app.task['baseurl']+url)
		html_doc = br.response().read()
		forms = [f for f in br.forms()]
		ctrl_names = [c.name for c in forms[0].controls]
		if debug=='debug' or debug=='verbose':
			print '[DEBUG] %d controls in'%len(ctrl_names), ctrl_names
		assert 'btnSearch' in ctrl_names, 'query_by_form failed for problematic login'
		print '[INFO ] query_by_form asserts that login passed.'
		self.app.task['stage'] = 'login_passed'
		
		# prepare a request
		only_GVTeachList_table = SoupStrainer(id="GVTeachList")
		soup = BeautifulSoup(html_doc, "html.parser", parse_only=only_GVTeachList_table, from_encoding="utf-8")
		td_tags = soup.findAll('td')
		if debug=='debug' or debug=='verbose':
			print '[DEBUG] %d <td> tag(s) found - ' % len(td_tags)

		# request body: %24 encodes dollar
		# <a id="GVTeachList_ctl02_lbnDatail" href="javascript:__doPostBack('GVTeachList$ctl02$lbnDatail','')">...</a>
		for td in td_tags:
			found = False
			strtd =  self.course_in(td, debug)
			if self.app.task['course']==strtd:
				a_tag = td.find_next('a')
				if debug=='debug' or debug=='verbose':
					print '[DEBUG] course found', a_tag
				found = True
				break
		
		if found:
			print '[INFO ] query_by_form asserts that course was found.'
			self.app.task['stage'] = 'query_coursefound'
		else:
			self.app.task['stage'] = 'query_coursenotfound'
		assert found == True, 'query_by_form failed for a problematic course %s'%self.app.task['course']

		a_href = a_tag['href']
		event_target=re.search('(?<=\')\S+',a_href.split(',')[0]).group(0).strip('\'')
		if debug=='debug' or debug=='verbose':
			print '[DEBUG] __EVENTTARGET %s' % event_target
		viewState = re.findall('<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*)" />',html_doc)
		viewStateEnerator = re.findall('<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*)" />',html_doc)
		eventValidation = re.findall('<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*)" />',html_doc)
		# Find the scorein form
		br.select_form(name='form1') 
		br.set_all_readonly(False)
		br.form["__EVENTTARGET"] = event_target 
		br.form["__EVENTARGUMENT"] = '' 
		br.form["__VIEWSTATE"] = viewState[0]
		br.form["__VIEWSTATEGENERATOR"] = viewStateEnerator[0]
		br.form["__EVENTVALIDATION"] = eventValidation[0]
		#Note the selection in the form has to be set by a list
		br.form["ddlYear"] = [ddlYear]
		br.form["ddlTerm"] = [ddlTerm]
		#Must disable btnSearch
		ctrl = br.form.find_control("btnSearch")
		ctrl.disabled = True
		# Submit the form
		br.submit()
		self.app.task['stage'] = 'query_passed'
		print '[INFO ] query_by_form asserts that query passed.'

		if debug=='verbose':
			html_doc = br.response().read()
			print html_doc

	"""Input the scores""" 
	def load_scores(self, txtExamTime='2014/8/30', rblTag='1', txtComment='load by mechanize', debug='info'):
		print '[INFO ] load_scores start ...'
		#[1] submit by 'clicking' btnModifyScore
		html_doc = br.response().read()
		forms = [f for f in br.forms()]
		ctrl_names = [c.name for c in forms[0].controls]
		if debug=='debug' or debug=='verbose':
			print '[DEBUG] %d controls in'%len(ctrl_names), ctrl_names
		assert 'btnModifyScore' in ctrl_names
		print '[INFO ] load_scores asserts that query passed.'
		self.app.task['stage'] = 'query_passed'

		#To please form validation of ASP.net WebForm
		viewState = re.findall('<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*)" />',html_doc)
		viewStateEnerator = re.findall('<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*)" />',html_doc)
		eventValidation = re.findall('<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*)" />',html_doc)
		# Submit with named control btnModifyScore
		br.select_form(nr=0) 
		br.set_all_readonly(False)
		br.form["__VIEWSTATE"] = viewState[0]
		br.form["__VIEWSTATEGENERATOR"] = viewStateEnerator[0]
		br.form["__EVENTVALIDATION"] = eventValidation[0]
		response = br.submit(name='btnModifyScore')

		#[2] Confirm examination time
		forms = [f for f in br.forms()]
		ctrl_names = [c.name for c in forms[0].controls]
		print '[DEBUG] %d controls in'%len(forms[0].controls), ctrl_names
		assert 'CsfBtnAddTime' in ctrl_names
		br.select_form(nr=0) 
		br.set_all_readonly(False)
		br.form["CsftxtExamTime"] = txtExamTime
		br.form["CsfrblTag"] = [rblTag]
		br.form["CsftxtComment"] = txtComment
		# Submit with named control CsfBtnAddTime
		response = br.submit(name='CsfBtnAddTime')

		#[3] Input the scores one by one and then submit
		forms = [f for f in br.forms()]
		ctrl_names = [c.name for c in forms[0].controls]
		if debug=='debug' or debug=='verbose':
			print '[DEBUG] %d controls in'%len(ctrl_names), ctrl_names
		assert 'Button2' in ctrl_names
		print '[INFO ] load_scores asserts a feasible submission.'
		self.app.task['stage'] = 'load_canbesubmitted'
		br.select_form(nr=0) 
		br.set_all_readonly(False)
		# e.g. GVModifyScore$ctl02$txtScore
		nice_ctrl_names = [c for c in ctrl_names if re.search('txtScore$', c) != None]
		if debug=='debug' or debug=='verbose':
			print '[DEBUG] %d nice controls in'%len(nice_ctrl_names), nice_ctrl_names
		assert 'GVModifyScore$ctl02$txtScore' in nice_ctrl_names
		print '[INFO ] load_scores asserts that score-control found.'
		self.app.task['stage'] = 'load_controlfound'

		scoresin = []
		self.read_scores(scoresin)
		for i,ctrl in enumerate(nice_ctrl_names):
			br.form[ctrl] = scoresin[i]
			txt =  ctrl.split('$')
			br.form[txt[0]+'$'+txt[1]+"$txtComment"] = txtComment
		# Submit with named control Button2
		response = br.submit(name='Button2')
		print '[INFO ] load_scores asserts that all scores are loaded.'
		self.app.task['stage'] = 'load_scoreloaded'
