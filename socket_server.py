
from socketserver import *

class Server(ForkingMixIn,TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(10).decode()
            print(data)
            self.request.send(b'ranger that')

server = Server(('localhost',8889),Handler)
server.serve_forever()