#!/usr/bin/env python3
# File: UdpClient.py
# MISSION: Demonstrate UDP Messaging Source / Client.
# Author: Randall Nagy
# Website: Soft9000.com

# CAVEAT: Do not run BOTH scripts in the IDE.
# Best to run the server script at the CLI.

import socket

server_socket       = ("127.0.0.1", 9000)
max_sz              = 1024

def send(request):
    msg_buffer = str.encode(request)
    # Creating a UDP Client:
    udp_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Sending a datagram to a UDP Server:
    udp_client.sendto(msg_buffer, server_socket)
    # Get the Server's response:
    response = udp_client.recvfrom(max_sz)
    print(f"Response: [{response}]")
    udp_client.close()

send("Client's Hello!")
