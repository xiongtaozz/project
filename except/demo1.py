try:  
    floatnum = float(input("Please input a float:"))  
    intnum = int(floatnum)  
    print 100/intnum  
except ZeroDivisionError:  
    print "Error:you must input a float num which is large or equal then 1!"  
except ValueError:  
    print "Error:you must input a float num!"  
 