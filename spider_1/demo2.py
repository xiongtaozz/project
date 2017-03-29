import socket
import threading
import time

# def tcplink(sock, addr):
#     print "Accept new connection from %s:%s..." % addr
#     sock.send('Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if data == "exit" or not data:
#             break
#         sock.send("Hello, %s" % data)
#     sock.close()
#     print "Connection from %s:%s closed." % addr

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 9000))
    print s.recv(1024)
    for data in ['Michael', 'www', 'eee']:
        print data
        s.send(data)
        print s.recv(1024)
    s.send("exit")
    s.close()