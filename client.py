from socket import *


connfd = socket()
connfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
connfd.connect(('127.0.0.1',8888))
while True:
    a = input('input:')
    if a == '':
        break
    connfd.send(a.encode())
    data = connfd.recv(1024)
    print(data.decode())
    connfd.close()