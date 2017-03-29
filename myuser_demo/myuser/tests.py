#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
account='18218086670'
pwd='888888'
url='http://pvmanage.cardspay.cn'
def openbrowser():
    '''
     返回浏览器的句柄
    '''
    driver = webdriver.Chrome()
    time.sleep(1)
    return driver
def openurl(driver,url):
    '''
     在当前打开的浏览器中，输入url地址
    '''
    driver.get(url)
    time.sleep(1)
    # driver.maximize_window()
def findelement(driver,arg):
    ele1=driver.find_element_by_id(arg['account'])
    # usele.click()
    ele2=driver.find_element_by_name(arg['pwd'])
    # pwdele.click()
    ele3=driver.find_element_by_id(arg['loginid'])
    # loginele.click()
    return ele1,ele2,ele3
def sendkey(ele_tuple,arg):
    '''
    ele_tuple是我们返回来的元素组成的元组
    account_dict是我们的数据,分别是uname,pwd
    '''
    listkey=['uname','pwd']
    n=0
    for k in listkey:
        ele_tuple[n].send_keys('')
        ele_tuple[n].clear()
        ele_tuple[n].send_keys(arg[k])
        n+=1
    ele_tuple[2].click()
def login_test():
    driver=openbrowser()   # 打开谷歌浏览器
    openurl(driver,url)  # 输入网址
    a_dict={'account':'username','pwd':'password','loginid':'login_btn'}#所有的元素构成的一个字典
    ele_tuple=findelement(driver,a_dict)#将查找到并返回的元素构成一个元组
    account_dict={'uname':account,'pwd':pwd}
    sendkey(ele_tuple,account_dict)
   
    # ele4=driver.find_element_by_class_name('sidebar-title').click()
    # ele5=driver.find_element_by_link_text(u'基本信息').click()
if __name__=='__main__':
    login_test()