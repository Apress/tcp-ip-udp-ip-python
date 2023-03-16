#!/usr/bin/env python3
import socket
# MISSION: Demonstrate that clients still work the same!
# Author: Randall Nagy
# Website: Soft9000.com

server_socket       = ("127.0.0.1", 9000)
max_sz              = 1024

def send(request):
    msg_buffer = str.encode(request)
    udp_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_client.sendto(msg_buffer, server_socket)
    response = udp_client.recvfrom(max_sz)
    print(f"Response: [{response}]")
    udp_client.close()

send("Client's Hello!")
