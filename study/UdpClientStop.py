#!/usr/bin/env python3
# MISSION: Demonstrate UDP Messaging Source / Client [STOP REQUEST]
# Author: Randall Nagy
# Website: Soft9000.com

# CAVEAT: Do not run BOTH scripts in the IDE.
# Best to run the server script at the CLI.

import socket

server_socket       = ("192.168.1.24", 9000)
max_sz              = 1024

def send(request="stop"):
    msg_buffer = str.encode(request)
    # Creating a UDP Client:
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Sendng a datagram to a UDP Server:
    udp_client.sendto(msg_buffer, server_socket)
    # Get the Server's response:
    response = udp_client.recvfrom(max_sz)
    print(f"Response: [{response}]")

send("Client's Hello!")
#send()
