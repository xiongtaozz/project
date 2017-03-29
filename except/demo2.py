#第一：try不仅捕获异常，而且会恢复执行
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
    

#第二：无论try是否发生异常，finally总会执行
#def catcher():  
    #try:  
        #fetcher(x, 4)  
    #finally:  
        #print 'after fecth'  
#第三：try无异常，才会执行else
#def catcher():  
    #try:  
        #fetcher(x, 4)  
    #except:  
        #print "got exception"  
    #else:  
        #print "not exception" 
#注意：else作用：没有else语句，当执行完try语句后，无法知道是没有发生异常，还是发生了异常并被处理过了。
#通过else可以清楚的区分开。
#第四：利用raise传递异常
#def catcher():  
    #try:  
        #fetcher(x, 4)  
    #except:  
        ##print "got exception"  
        #raise Exception('hi here')
#第五：except(name1, name2)
#def catcher():  
    #try:  
        #fetcher(x, 4)  
    #except(TypeError, IndexError):  
        #print "got exception"  
    #else:  
        #print "not exception"  
#捕获列表列出的异常，进行处理。若except后无任何参数，则捕获所有异常。
#def catcher():  
    #try:  
        #fetcher(x, 4)  
    #except:  
        #print "got exception"  
        
catcher()