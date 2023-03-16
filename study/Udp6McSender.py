#!/usr/bin/env python3
# Mission: Send out SO_BROADCAST messages.
# Author: Randall Nagy
# Website: Soft9000.com

import Udp6Multicast

Udp6Multicast.broadcast("Testing...")
Udp6Multicast.broadcast("1...")
Udp6Multicast.broadcast("2...")
Udp6Multicast.broadcast("3...")
Udp6Multicast.broadcast("stop")
