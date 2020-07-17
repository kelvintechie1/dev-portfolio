#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# IP Prefix Generator
# By: Kelvin Tran

# Note: at the moment, only supports IPv4 prefixes - IPv6 support to be implemented

import ipaddress
import random
from tabulate import tabulate
import argparse # usage coming later
import csv # usage coming later
import io # usage coming later
import re # usage coming later

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

def inputOtherCriteria():
    print("Placeholder")

def GenerateIPv4Prefixes(number):
    counter = 0
    returnOutput = []

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

        outputAppend = []

        outputAppend.append(str(prefix := (ipaddress.IPv4Network((address := firstOctet + otherOctets[0] 
            + otherOctets[1] + otherOctets[2]) + "/" + prefixLength, strict=False))))
        outputAppend.append(str(prefix.netmask))
        outputAppend.append(str(address))
        returnOutput.append(outputAppend)

        counter += 1

    return returnOutput

def GenerateIPv6Prefixes(number, GlobalUnicast):
    """Note: This script assumes the validity of the IETF-estabished IPv6 unicast address assignments table 
    found here: https://www.iana.org/assignments/ipv6-unicast-address-assignments/ipv6-unicast-address-assignments.xhtml
    and therefore uses the 2000::/15 address block for address generation to avoid interfering with any reserved blocks,
    such as 2002::/16 for 6to4 IPv6 transition operations."""

    # Global unicast range - 2000::/15, Unique Local Range: fc00::/7
    # Other ranges not supported at this time.

    counter = 0
    returnOutput = []

    GlobalUnicast = True # troubleshooting - remove when finished

    if GlobalUnicast:
        range = ipaddress.IPv6Network("2000::/15")
    elif not GlobalUnicast:
        range = ipaddress.IPv6Network("fc00::/7")
    
    return returnOutput
    
def GenerateConfiguration():
    print("Placeholder")

def main():
    prefixNum = inputPrefixNum()

    if prefixNum[0] != 0:
        print("\n")
        print("IPv4 Networks: \n")
        print(tabulate(outputIPv4 := (GenerateIPv4Prefixes(prefixNum[0])), headers=["Network Prefix", "Subnet Mask", "Host Address"]))
    
    if prefixNum[1] != 0:
        print("\n")
        print("IPv6 Networks: \n")
        print("Support coming soon!") # replace with tabulate
        #print(tabulate(outputIPv6 := (GenerateIPv6Prefixes(prefixNum[1])), headers=["Network Prefix", "Host Address"]))


if __name__ == "__main__":
    main()
