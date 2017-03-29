from django.test import TestCase

# Create your tests here.

for x in xrange(10):


    if x < 9 and x >=3:
        print "  *"+(x-2)*"   "+"  *"
    else:
        print x * "  *"
    # if x-1 >= 4:
    #     print '  *'+(x-3)*' '+'  *'
    # elif x-1 == 3:
    #     print '  *' + ' '+'  *'
    # else:
    #     print (x-1)*'  *'


