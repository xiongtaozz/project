import urllib2
import urllib

def FileDemo(strs):

    f = open('html.txt','w')

    f.write(strs)

    f.close()

url = 'http://baidu.lecai.com/lottery/draw/sorts/ajax_get_draw_data.php?%s'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Cookie': '_lcas_uuid=877441277; _adwc=110406678; _adwr=110406678%230; Hm_lvt_9b75c2b57524b5988823a3dd66ccc8ca=1451219426; Hm_lpvt_9b75c2b57524b5988823a3dd66ccc8ca=1451223239; Hm_lvt_6c5523f20c6865769d31a32a219a6766=1451219426; Hm_lpvt_6c5523f20c6865769d31a32a219a6766=1451223239; _source=5591; _source_pid=0; _srcsig=ccbdb96c; _lhc_uuid=sp_567fd9dd6b2984.18417501; _adwb=110406678; _adwp=110406678.0544050426.1451219426.1451219426.1451223238.2',
    'Host':'baidu.lecai.com',
    'Referer':'http://baidu.lecai.com/lottery/draw/sorts/cqssc.php?phase=20151227085&agentId=5591',
    'User-Agent' :'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0X-Requested-WithXMLHttpRequest',
}
values = {'lottery_type':200 ,'date' :'2015-12-27'}
data = urllib.urlencode(values)
url = url % data
req = urllib2.Request(url=url,headers=headers)
res = urllib2.urlopen(req)
html = res.read()
FileDemo(html)
print html




