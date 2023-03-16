# File: 0xFFFF.py
# MISSION: Basic Concept Review [Binary Ranges]
# Author: Randall Nagy
# Website: Soft9000.com

z64K = 0xffff
for ss, bit in enumerate(bin(z64K)[2:],1):
    if not ss % 4:
        print(bit + '.', end='')
    else:
        print(bit, end='')

print()
print(z64K)
