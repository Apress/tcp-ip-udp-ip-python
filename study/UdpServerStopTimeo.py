#!/usr/bin/env python3
# MISSION: Demonstrate UDP Messaging Reception / Server [TIMEOUT]
# Author: Randall Nagy
# Website: Soft9000.com

# CAVEAT: Do not run BOTH scripts in the IDE.
# Best to run the server script at the CLI.

import socket, time

server_address  = "127.0.0.1"
port_server     = 9000
max_sz          = 1024

response       = "Hello UDP Client"
msg_buffer     = str.encode(response)

# Server: Create a datagram socket
udp_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to socket
udp_server.bind((server_address, port_server))
print("UDP Started.")

# Intercept incoming datagrams
print("\tUDP Server Listening...")
print(f"{udp_server.recvfrom(max_sz)}")
time.sleep(7)
print("UDP Stopped.")
udp_server.close()

