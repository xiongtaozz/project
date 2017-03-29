from twisted.internet import reactor
from twisted.enterprise import adbapi

# Please use your host, username and password for mysql

dbpool = adbapi.ConnectionPool("MySQLdb", db='test', user='******', passwd='******', 
    host='******', use_unicode=True, charset='utf8')
    
def _getAge(txn, user):
    txn.execute("select * from stu where name=%s", [user])
    results = txn.fetchall()
    if results:
        return results[0][2]
    else:
        return None
        
def get_age(user):
    return dbpool.runInteraction(_getAge, user)
    
def printResult(age):
    if age!=None:
        print age, "years old."
    else:
        print "No such name."
        
def printL(l):
    print "Total records:", l[0][0]
        
get_age("lisi").addCallback(printResult)
dbpool.runQuery("SELECT COUNT(*) FROM stu").addCallback(printL)

reactor.callLater(1,reactor.stop)
reactor.run()