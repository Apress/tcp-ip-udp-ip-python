#!/usr/bin/env python3
# MISSION: Demonstrate UDP Messaging Reception / Server
# Author: Randall Nagy
# Website: Soft9000.com

# CAVEAT: Do not run BOTH scripts in the IDE.
# Best to run the server script at the CLI.

import socket

server_address  = "127.0.0.1"
port_server     = 9000
max_sz          = 1024

# Server: Create a datagram socket
udp_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to socket
udp_server.bind((server_address, port_server))
print("UDP Started.")

# Intercept incoming datagrams
count = 0
while(True):
    print("\tUDP Server Listening...")
    request_set = udp_server.recvfrom(max_sz)
    count += 1
    print(f"\t{count}.) {request_set}")
    # Server's response to Client:
    udp_server.sendto(str.encode("ACK - Server"), request_set[1])
