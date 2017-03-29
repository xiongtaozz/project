# Echo client program
import socket

HOST = 'www.baidu.com'    # The remote host
PORT = 80              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: keep-alive\r\n\r\n')
data = s.recv(80960)
s.close()
print 'Received', repr(data)