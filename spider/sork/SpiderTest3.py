# -*- coding: utf-8 -*-
#模拟提交测试

import urllib
import urllib.request

url = "http://localhost:8000/addSave/"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Accept':'text/html, application/xhtml+xml, */*',
'Accept-Language':' zh-CN',
'Accept-Encoding':'gzip, deflate',
'Connection':'Keep-Alive',
'Cookie': 'csrftoken=92us53O087Xtn8OvEazZ5q2q58t6cECK'
}

values = {"csrfmiddlewaretoken":"92us53O087Xtn8OvEazZ5q2q58t6cECK",
          "txtID":"1234",
          "txtName":"你好",
          "txtNick":"111",
          "txtVip":"2"}
requestData = urllib.parse.urlencode(values)
print(requestData)
requestData = requestData.encode("utf8")

req = urllib.request.Request(url, requestData, headers)
resp = urllib.request.urlopen(req)
respBytes = resp.read()
print(respBytes.decode("utf8"))

