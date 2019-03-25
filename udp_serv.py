
import socket

sockfd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sockfd.bind(('localhost',8888))
data,addr = sockfd.recvfrom(1024)
print(data.decode())
print(addr)
sockfd.sendto(b'liyangshoudao',addr)
print('over')
sockfd.close()
