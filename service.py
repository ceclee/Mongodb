
from socket import *

socketfd = socket()
socketfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socketfd.bind(('127.0.0.1',8887))
socketfd.listen(5)

while True:
    print('wait for `````accept')
    conn,addr = socketfd.accept()
    print('accept!')
    print(addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())

        a = open('pow.txt','rt')
        print(a)
        b = a.read()
        print(b,end='')
        send1 = conn.send(b.encode())
        print('send:',send1)
        a.close()

    conn.close()

socketfd.close()
