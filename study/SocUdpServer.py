#!/usr/bin/env python3
# MISSION: Demonstrate the basic socketserver framework opportunities
# Author: Randall Nagy
# Website: Soft9000.com

import socketserver

server_port         = 9000
server_socket       = ("127.0.0.1", server_port)
max_sz              = 1024

def serve(zHandler):
    server = socketserver.UDPServer(server_socket, zHandler)
    print(f"Monitoring: {type(zHandler)}")
    server.serve_forever()

class MyDatagramHandler(socketserver.DatagramRequestHandler):
    '''
    A BaseRequestHandler uses setup() & finish() to provide self.rfile
    and self.wfile attributes.
    '''
    def setup(self):
        print("SETUP!")
        super().setup()

    def finish(self):
        print("FINISH!")
        super().finish()
        
    def handle(self):
        print(f"Request from: {self.client_address[0]}")
        print(f"Request: {self.rfile.read(max_sz)}")
        print(f"Write: [{self.wfile.write(b'ACK!')}]") 

def monitor():
    serve(MyDatagramHandler)

monitor()

