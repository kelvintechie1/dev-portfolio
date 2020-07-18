#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# IP Prefix Generator
# By: Kelvin Tran

import ipaddress
import random
from tabulate import tabulate
import argparse # usage coming later
import csv # usage coming later
import io # usage coming later

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

        randomUInt = (random.getrandbits(32)) & 0xffffffff

        prefixLength = str(random.randint(1, 32))   

        appendValue = []
        
        appendValue.append(str(prefix := (ipaddress.IPv4Network(str(address := ipaddress.IPv4Address(randomUInt))
            + "/" + prefixLength, strict=False))))
        appendValue.append(str(prefix.netmask))
        appendValue.append(str(address))

        if (((private and (address.is_global or address.is_private)) or (not private and (address.is_global and not address.is_private))) 
                and not address.is_multicast and not address.is_reserved and not address.is_unspecified and not address.is_link_local 
                and not address.is_loopback):
            returnOutput.append(appendValue)
        else:
            continue

        counter += 1

    return returnOutput

def GenerateIPv6Prefixes(number, GlobalUnicast, extendedPL, firstHost):

    counter = 0
    returnOutput = []

    while counter < number:

        randomUInt = (random.getrandbits(128)) & 0xffffffffffffffffffffffffffffffff

        if extendedPL:
            prefixLength = str(random.randint(1, 126))
        if not extendedPL:
            prefixLength = str(random.randint(32, 126))

        appendValue = []

        appendValue.append(prefix := ipaddress.IPv6Network(str(address := ipaddress.IPv6Address(randomUInt)) 
            + "/" + prefixLength, strict=False))

        if (((GlobalUnicast and prefix.is_global)
                or (not GlobalUnicast and address.is_private))
                and not address.is_link_local and not address.is_loopback and not address.is_multicast
                and not address.is_reserved and not address.is_site_local and not address.is_unspecified):
            returnOutput.append(appendValue)
        else:
            continue

        if firstHost:
            appendValue.append(prefix[1])
        elif not firstHost:
            appendValue.append(address)
        
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
        print("IPv4 Networks [" + str(prefixNum[0]) + "]: \n")
        print(tabulate((GenerateIPv4Prefixes(number=prefixNum[0], private=private)), 
            headers=["Network Prefix", "Subnet Mask", "Host Address"]))
    
    if prefixNum[1] != 0:
        print("\n")
        print("IPv6 Networks [" + str(prefixNum[1]) + "]: \n")
        print(tabulate((GenerateIPv6Prefixes(number=prefixNum[1], GlobalUnicast=GlobalUnicast, extendedPL=extendedPL, 
            firstHost=firstHost)), headers=["Network Prefix", "Host Address"]))


if __name__ == "__main__":
    main()
