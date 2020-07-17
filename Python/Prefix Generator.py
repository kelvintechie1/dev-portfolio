#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# IP Prefix Generator
# By: Kelvin Tran

# Note: at the moment, only supports IPv4 prefixes - IPv6 support to be implemented

import ipaddress
import random
import argparse
import csv
import io
import re

# User inputs number of prefixes
def inputPrefixNum():
    successful = False
    while not successful:
        try:
            prefixNum = []
            prefixNum.append(int(input("How many IPv4 prefixes do you want to generate? ")))
            prefixNum.append(int(input("How many IPv6 prefixes do you want to generate? ")))
            successful = True
        except (ValueError,TypeError):
            print("Please enter a valid number - integers only.")
            continue
    return prefixNum

def GenerateIPv4Prefixes(number):
    counter = 0
    prefixes = []
    while counter < number:
        firstOctet = (str(random.randint(1, 223)) + ".")
        otherOctets = []
        octet = 1
        while octet < 4:
            value = str(random.randint(1,255))
            if octet < 3:
                value = value + "."
            otherOctets.append(value)
            octet += 1
        prefixLength = str(random.randint(1, 32))
        prefixes.append(str(ipaddress.IPv4Network(address := (firstOctet + otherOctets[0] + otherOctets[1]
            + otherOctets[2] + "/" + prefixLength), strict=False))
            + " - Host Address: " + address)
        counter += 1
    return prefixes

def GenerateIPv6Prefixes(number):
    print("Feature coming soon.")
    # Add global unicast (2000::/3) or unique local (fc00::/7)
    


def main():
    prefixNum = inputPrefixNum()
    for item in enumerate(prefixes := (GenerateIPv4Prefixes(prefixNum[0]))):
        print(prefixes[item[0]])

if __name__ == "__main__":
    main()
