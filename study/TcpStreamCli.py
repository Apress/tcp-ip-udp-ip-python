#!/usr/bin/env python3
# MISSION: Demonstrate the TCP/IP connection basics.
# Author: Randall Nagy
# Website: Soft9000.com

import TcpStreams

while True:
    print("`q` to quit..")
    request = input("\tSend: ")
    if request == 'q':
        break
    TcpStreams.broadcast(request)

print("\n\nDone!")
