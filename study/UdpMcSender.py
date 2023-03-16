#!/usr/bin/env python3
# MISSION: Send out SO_BROADCAST messages.
# Author: Randall Nagy
# Website: Soft9000.com

import UdpMulticast

UdpMulticast.broadcast("Testing...")
UdpMulticast.broadcast("1...")
UdpMulticast.broadcast("2...")
UdpMulticast.broadcast("3...")
UdpMulticast.broadcast("stop")
