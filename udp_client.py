
from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)
a = input('input:')
sockfd.sendto(a.encode(),('localhost',8888))
data,addr = sockfd.recvfrom(1024)
print(data.decode(),addr)
sockfd.close()