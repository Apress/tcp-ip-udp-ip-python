# File: v4_masks.py
# MISSION: Basic Concept Review [Reporting & Formatting]
# Author: Randall Nagy
# Website: Soft9000.com

for i in 0, 255, 65535, 16777215:
    print(f"{hex(i):>15} {bin(i):^30} {i}")
