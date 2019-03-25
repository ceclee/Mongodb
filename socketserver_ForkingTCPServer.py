
from socketserver import *

class A(ForkingMixIn,TCPServer):
    pass

class B(StreamRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(10).decode()
            print(data)
            self.request.send(b'ranger that')

server = A(('localhost',8889),B)
server.serve_forever()