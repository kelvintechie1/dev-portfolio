#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# IP Prefix Generator
# By: Kelvin Tran

from tabulate import tabulate
import ipaddress
import random
import csv
import io
import sys
import argparse # usage coming later
import json # usage coming later

# User inputs number of prefixes
def inputPrefixNum():
    successful = False
    while not successful:
        try:
            prefixNum = []
            IPv4Count = input("How many IPv4 prefixes do you want to generate? (Default: 0) ")
            if IPv4Count == "":
                prefixNum.append(0)
            else:
                prefixNum.append(int(IPv4Count))
            IPv6Count = input("How many IPv6 prefixes do you want to generate? (Default: 0) ")
            if IPv6Count == "":
                prefixNum.append(0)
            else:
                prefixNum.append(int(IPv6Count))
            successful = True
        except (ValueError,TypeError) as error:
            print("Please enter a valid number - integers only. - Error: " + str(error))
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
        IPv4Responses.append(input("Include private addresses [Y/N] (Default: N): "))
    elif not IPv4Selected:
        IPv4Responses = None

    if IPv6Selected:
        IPv6Responses.append(input("Global Unicast [1] or Unique Local Addresses [2] (Default: 1): "))
        if IPv6Responses[0] == "1":
            IPv6Responses.append(input("Extended global unicast range (2000::/3) [1] or restricted range (2000::/15) [2] (Default: 1): "))
        else:
            IPv6Responses.append(None)
        IPv6Responses.append(input("Use standard (32-128) [1] or extended (1-128) [2] prefix length range (Default: 1): "))
        IPv6Responses.append(input("Make host address the first in the subnet [Y/N] (Default: N): "))
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

def GenerateIPv6Prefixes(number, GlobalUnicast, extendedPL, firstHost, restrictedGURange):

    counter = 0
    returnOutput = []

    while counter < number:

        if restrictedGURange:
            randomUInt = int((str(random.randint(2000,2001))) + (hex((random.getrandbits(112)) & 0xffffffffffffffffffffffffffff))[2:], base=16)
        else:
            randomUInt = (random.getrandbits(128)) & 0xffffffffffffffffffffffffffffffff

        if extendedPL:
            prefixLength = str(random.randint(1, 128))
        if not extendedPL:
            prefixLength = str(random.randint(32, 128))

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
            appendValue.append(prefix[0])
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
        
        if options[1][1] == "2":
            restrictedGURange = True
        else:
            restrictedGURange = False

        if options[1][2].upper() == "2":
            extendedPL = True
        else:
            extendedPL = False

        if options[1][3].upper() == "Y":
            firstHost = True
        else:
            firstHost = False

    if prefixNum[0] != 0:
        print("\n")
        print("IPv4 Networks [" + str(prefixNum[0]) + "]: \n")
        print(tabulate((IPv4CSV := GenerateIPv4Prefixes(number=prefixNum[0], private=private)), 
            headers=["Network Prefix", "Subnet Mask", "Host Address"]))
    
    if prefixNum[1] != 0:
        print("\n")
        print("IPv6 Networks [" + str(prefixNum[1]) + "]: \n")
        print(tabulate((IPv6CSV := GenerateIPv6Prefixes(number=prefixNum[1], GlobalUnicast=GlobalUnicast, extendedPL=extendedPL, 
            firstHost=firstHost, restrictedGURange=restrictedGURange)), headers=["Network Prefix", "Host Address"]))
    
    if prefixNum[0] == 0 and prefixNum[1] == 0:
        print("You provided 0 for both values. Please re-run and provide a non-zero number for one or more address families.")
        sys.exit()

    saveAsCSV = input("Do you want to save these results as a CSV file? [Y/N] ")
    if saveAsCSV.upper() == "Y":
        print("WARNING: Providing a file path to a file that already exists will result in that file being overwritten.")

        IPv4filePath = input("IPv4 - Provide an ABSOLUTE file path including the file name and csv extension. Default: ipv4address.csv in the same folder as your script. --- ")
        IPv6filePath = input("IPv6 - Provide an ABSOLUTE file path including the file name and csv extension. Default: ipv6address.csv in the same folder as your script. --- ")

        if IPv4filePath is None or IPv4filePath == "":
            IPv4filePath = "ipv4address.csv"
        if IPv6filePath is None or IPv6filePath == "":
            IPv6filePath = "ipv6address.csv"
        
        successful = False
        while not successful:
            try:
                with open(IPv4filePath, 'w') as IPv4csvFile:
                    writer = csv.writer(IPv4csvFile, delimiter=",", quotechar="\"")
                    writer.writerow(["Network Prefix", "Subnet Mask", "Host Address"])
                    for item in enumerate(IPv4CSV):
                        writer.writerow(item[1])
                with open(IPv6filePath, 'w') as IPv6csvFile:
                    writer = csv.writer(IPv6csvFile, delimiter=",", quotechar="\"")
                    writer.writerow(["Network Prefix", "Host Address"])
                    for item in enumerate(IPv6CSV):
                        writer.writerow(item[1])
                successful = True
            except IOError as error:
                print("Error: " + str(error))
                sys.exit()


if __name__ == "__main__":
    main()
