# File: masks_to_cidr.py
# MISSION: Basic Concept Review [Binary Reporting]
# Author: Randall Nagy
# Website: Soft9000.com

def mask_to_cidr(dot_mask):
    results = 0
    for bits in dot_mask.split("."):
        results += bin(int(bits)).count('1')
    return results

for mask in '255.0.0.0',\
	    '255.255.0.0',\
	    '255.255.255.255':
    print(mask_to_cidr(mask))

