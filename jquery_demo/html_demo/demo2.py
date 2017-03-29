import sys
import os
import socket

b=os.path.dirname(__file__)
a=sys.argv[0]
print a[len(b)+1:len(a)]

print socket.gethostname()

