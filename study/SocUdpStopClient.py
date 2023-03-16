#!/usr/bin/env python3
# MISSION: Demonstrate UDP Messaging [STOP + RESPONSE]
# Author: Randall Nagy
# Website: Soft9000.com

import socket

server_socket       = ("127.0.0.1", 9000)
max_sz              = 1024

def send(request="stop"):
    msg_buffer = str.encode(request)
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_client.sendto(msg_buffer, server_socket)
    if request != 'stop':
        response = udp_client.recvfrom(max_sz)
        print(f"Response: [{response}]")
    else:
        print("Shutdown request was sent.")

send("CHello 001!")
send("CHello 002!")
send()
