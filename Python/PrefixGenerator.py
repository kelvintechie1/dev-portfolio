#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# IP Prefix Generator
# By: Kelvin Tran

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

def inputOtherCriteria(IPv4Num, IPv6Num):
    IPv4Responses = []
    IPv6Responses = []

    IPv4Selected = False
    IPv6Selected = False

    if IPv4Num != 0:
        IPv4Selected = True
    if IPv6Num != 0:
        IPv6Selected = True
    
    if IPv4Selected:
        IPv4Responses.append(input("Include private addresses [Y/N]: "))
    elif not IPv4Selected:
        IPv4Responses = None

    if IPv6Selected:
        IPv6Responses.append(input("Global Unicast [1] or Unique Local Addresses [2]: "))
        IPv6Responses.append(input("Use standard (32-128) [1] or extended (1-128) [2] prefix length range: "))
        IPv6Responses.append(input("Make host address the first in the subnet [Y/N]: "))
    elif not IPv6Selected:
        IPv6Responses = None
    
    return [IPv4Responses, IPv6Responses]

def GenerateIPv4Prefixes(number, private):
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

        appendValue = []

        appendValue.append(str(prefix := (ipaddress.IPv4Network((address := firstOctet + otherOctets[0] 
            + otherOctets[1] + otherOctets[2]) + "/" + prefixLength, strict=False))))
        appendValue.append(str(prefix.netmask))
        appendValue.append(str(address))
        returnOutput.append(appendValue)

        counter += 1

    return returnOutput

def GenerateIPv6Prefixes(number, GlobalUnicast, extendedPL, firstHost):
    """Note: This script assumes the validity of the IETF-estabished IPv6 unicast address assignments table 
    found here: https://www.iana.org/assignments/ipv6-unicast-address-assignments/ipv6-unicast-address-assignments.xhtml
    and therefore uses the 2000::/15 address block for address generation to avoid interfering with any reserved blocks,
    such as 2002::/16 for 6to4 IPv6 transition operations."""

    # Global unicast range - 2000::/15, Unique Local Range: fc00::/7
    # Other ranges not supported at this time.

    counter = 0
    returnOutput = []

    while counter < number:

        if GlobalUnicast:
            range = ipaddress.IPv6Network("2000::/15")
        elif not GlobalUnicast:
            range = ipaddress.IPv6Network("fc00::/7")
        
        chooseFirstGroup = random.randint(0,1)
        if GlobalUnicast:
            if chooseFirstGroup == 0:
                firstGroup = "2000:"
            elif chooseFirstGroup == 1:
                firstGroup = "2001:"
        elif not GlobalUnicast:
            if chooseFirstGroup == 0:
                firstGroup = "FC00:"
            elif chooseFirstGroup == 1:
                firstGroup == "FD00:"

        otherGroups = []

        groupsCounter = 1
        while groupsCounter < 8:
            value = str(hex(random.randint(0, 65535))[2:6])  # [2:6] in order to exclude the hex identifier (0x)
            if groupsCounter < 7:
                value = value + ":"
            otherGroups.append(value)
            groupsCounter += 1

        # Feature Idea: allow custom prefix length ranges
        if extendedPL:
            prefixLength = str(random.randint(1, 128))
        if not extendedPL:
            prefixLength = str(random.randint(32, 128))

        appendValue = []
        appendValue.append(ipaddress.IPv6Network((address := firstGroup + otherGroups[0] + otherGroups[1]
            + otherGroups[2] + otherGroups[3] + otherGroups[4] + otherGroups[5] + otherGroups[6]) + "/" + prefixLength, strict=False))
        
        if firstHost:
            appendValue.append(ipaddress.IPv6Address(next(appendValue[0].hosts())))
        elif not firstHost:
            appendValue.append(ipaddress.IPv6Address(address))

        returnOutput.append(appendValue)
        
        counter += 1

    return returnOutput
    
def GenerateIOSConfiguration():
    print("Placeholder")

def GenerateJUNOSConfiguration():
    print("Placeholder")

def main():
    prefixNum = inputPrefixNum()
    options = inputOtherCriteria(prefixNum[0], prefixNum[1])

    if options[0] is not None:
        if options[0][0].upper() == "Y":
            private = True
        else:
            private = False
        
    if options[1] is not None:
        if options[1][0].upper() == "2":
            GlobalUnicast = False
        else:
            GlobalUnicast = True

        if options[1][1].upper() == "2":
            extendedPL = True
        else:
            extendedPL = False

        if options[1][2].upper() == "Y":
            firstHost = True
        else:
            firstHost = False

    if prefixNum[0] != 0:
        print("\n")
        print("IPv4 Networks: \n")
        print(tabulate(outputIPv4 := (GenerateIPv4Prefixes(number=prefixNum[0], private=private)), headers=["Network Prefix", "Subnet Mask", "Host Address"]))
    
    if prefixNum[1] != 0:
        print("\n")
        print("IPv6 Networks: \n")
        print(tabulate(outputIPv6 := (GenerateIPv6Prefixes(number=prefixNum[1], GlobalUnicast=GlobalUnicast, extendedPL=extendedPL, 
            firstHost=firstHost)), headers=["Network Prefix", "Host Address"]))


if __name__ == "__main__":
    main()
