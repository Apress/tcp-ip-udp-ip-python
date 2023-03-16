#!/usr/bin/env python3
# MISSION: Demonstrate the TCP/IP connection basics.
# Author: Randall Nagy
# Website: Soft9000.com

import socket

server_port         = 9000
server_socket       = ("127.0.0.1", server_port)
max_sz              = 1024

def monitor():
    # Creating a TCP/IP receiver:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(server_socket)
        while True:
            print(f'Monitoring [{sock.getsockname()}]')
            sock.listen()
            conn, addr = sock.accept()
            with conn:
                print('Message from', addr)
                while True:
                    data = conn.recv(max_sz)
                    if not data:
                        break
                    conn.sendall(b'ACK: [' + data + b']')

def broadcast(request):
    print(f"Broadcasting [{request}]")
    msg_buffer = str.encode(request)
    # Creating a TCP/IP Client:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_socket)
        sock.sendall(msg_buffer)
        data = sock.recv(max_sz)
    print(f'Received [{data}]')

