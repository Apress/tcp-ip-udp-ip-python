#!/usr/bin/env python3
# MISSION: Demonstrate UDP Messaging Source / Client [Defaults]
# Author: Randall Nagy
# Website: Soft9000.com

# CAVEAT: Do not run BOTH scripts in the IDE.
# Best to run the server script at the CLI.

import socket

server_socket       = ("127.0.0.1", 9000)
max_sz              = 1024

def send(request='stop', wait=100.0):
    msg_buffer = str.encode(request)
    # Creating a UDP Client:
    udp_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_client.settimeout(wait)
    # Sending a datagram to a UDP Server:
    udp_client.sendto(msg_buffer, server_socket)
    # Get the Server's response:
    try:
        response = udp_client.recvfrom(max_sz)
        print(f"Response: [{response}]")
    except Exception as ex:
        print(ex)
        print("Retrying ...")
        udp_client.settimeout(100.0)
        udp_client.sendto(msg_buffer, server_socket)
        response = udp_client.recvfrom(max_sz)
        print(f"Response 1: [{response}]")
        response = udp_client.recvfrom(max_sz)
        print(f"Response 2: [{response}]")
    finally:
        udp_client.close()

send("Client's Hello!", 2.0)
#send()
