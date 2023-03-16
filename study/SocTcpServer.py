#!/usr/bin/env python3
# MISSION: Demonstrate basic socketserver framework options
# Author: Randall Nagy
# Website: Soft9000.com

import socketserver

server_port         = 9000
server_socket       = ("127.0.0.1", server_port)
max_sz              = 1024

def serve(zHandler):
    server = socketserver.TCPServer(server_socket, zHandler)
    server.serve_forever()

class MyStreamHandler(socketserver.StreamRequestHandler):
    '''
    A BaseRequestHandler uses setup() & finish() to provide self.rfile
    and self.wfile attributes. The self.rfile and self.wfile attributes
    can be read or written, respectively, to get the request data or
    return data to the client.
    '''
    def setup(self):
        print("SETUP!")

    def finish(self):
        print("FINISH!")
        
    def handle(self):
        print(f"Request from: {self.client_address[0]}")
        print(f"Request: {self.request}")
        print(f"Data: [{self.request.recv(max_sz)}]") 
        self.request.sendall(b"ACK!")

def monitor():
    serve(MyStreamHandler)

monitor()

