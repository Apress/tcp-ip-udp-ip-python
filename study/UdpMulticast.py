#!/usr/bin/env python3
# MISSION: Send, and monitor, SO_BROADCAST messages.
# Author: Randall Nagy
# Website: Soft9000.com

import socket

server_port         = 9000
server_socket       = ("255.255.255.255", server_port)
max_sz              = 1024

def monitor():
    # Creating a UDP receiver:
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    sock.bind(("", server_port))
    # Monitoring broadcasts:
    while True:
        print("Waiting...")
        request = sock.recvfrom(max_sz)
        print(f"Message: [{request}]")
        if request[0] == b'stop':
            sock.close()
            return

def broadcast(request):
    print(f"Broadcasting [{request}]")
    msg_buffer = str.encode(request)
    # Creating a UDP Client:
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    # Broadcasting a datagram:
    sock.sendto(msg_buffer, server_socket)
    sock.close()
