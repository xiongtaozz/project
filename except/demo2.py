#��һ��try���������쳣�����һ�ָ�ִ��
#def catcher():  
    #try:  
        #fetcher(x, 4)  
    #except:  
        #pass
        ##print "got exception" 
    #else:
        #print '222'
    #finally:
        #print '11111'
    #print "continuing" 
    

#�ڶ�������try�Ƿ����쳣��finally�ܻ�ִ��
#def catcher():  
    #try:  
        #fetcher(x, 4)  
    #finally:  
        #print 'after fecth'  
#������try���쳣���Ż�ִ��else
#def catcher():  
    #try:  
        #fetcher(x, 4)  
    #except:  
        #print "got exception"  
    #else:  
        #print "not exception" 
#ע�⣺else���ã�û��else��䣬��ִ����try�����޷�֪����û�з����쳣�����Ƿ������쳣����������ˡ�
#ͨ��else������������ֿ���
#���ģ�����raise�����쳣
#def catcher():  
    #try:  
        #fetcher(x, 4)  
    #except:  
        ##print "got exception"  
        #raise Exception('hi here')
#���壺except(name1, name2)
#def catcher():  
    #try:  
        #fetcher(x, 4)  
    #except(TypeError, IndexError):  
        #print "got exception"  
    #else:  
        #print "not exception"  
#�����б��г����쳣�����д�����except�����κβ������򲶻������쳣��
#def catcher():  
    #try:  
        #fetcher(x, 4)  
    #except:  
        #print "got exception"  
        
catcher()