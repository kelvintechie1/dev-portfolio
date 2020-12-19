"""IP Multicast to MAC Address Quiz Game
Created by: Kelvin Tran
Github: https://www.github.com/kelvintechie1"""

# Import necessary libraries
from ipaddress import *
import random
import re

# Create variable w/ IPv4 multicast block
mcastv4 = IPv4Network('224.0.0.0/8')
# Create variable w/ IPv6 multicast block
mcastv6 = IPv6Network('FF00::/8')


def ChooseMode():
    while True:
        print("1 = IPv4 only\n2 = IPv6 only\n3 = IPv4 and IPv6")
        try:
            userMode = int(input("What mode would you like to play? Type the number associated w/ the mode (1/2/3) "))
            if userMode not in [1, 2, 3]:
                print("Please enter 1, 2, or 3.")
                continue
            return userMode
        except ValueError as e:
            print("Please enter a proper integer.")
            continue


def ChooseTotal():
    while True:
        try:
            userMode = int(input("How many total questions do you want? "))
            return userMode
        except ValueError as e:
            print("Please enter a proper integer.")
            continue


def GenerateAddress(mode, v4, v6):
    addresses = {}
    if mode in [1, 3]:
        addresses[4] = v4[random.randint(0, v4.num_addresses)]
    if mode in [2, 3]:
        addresses[6] = v6[random.randint(0, v6.num_addresses)]
    return addresses


def GenerateMAC(address):
    returnString = ""
    addressType = str(type(address))
    if bool(re.match(r'.*IPv4Address.*', addressType)):
        returnString += "01:00:5E:"

        for i in range(len(lastThreeOctets := (str(address).split('.')[1:4]))):
            lastThreeOctets[i] = int(lastThreeOctets[i])

        if lastThreeOctets[0] < 128:
            lastThreeOctets[0] += 128
        elif lastThreeOctets[0] >= 128:
            lastThreeOctets[0] -= 128

        for i in lastThreeOctets:
            returnString += "{:02x}:".format(i)


    elif bool(re.match(r'.*IPv6Address.*', addressType)):
        returnString += "33:33:"

        for i in range(len(lastTwoQuartets := (str(address).split(':')[6:8]))):
            returnString += lastTwoQuartets[i][0:2] + ":" + lastTwoQuartets[i][2:4] + ":"

    return returnString[:17].upper()


def CheckAnswer(mac, address):
    correctStatus = None
    while correctStatus is None:
        print("Answer in XX:XX:XX:XX:XX:XX format:")
        answer = input("What is the MAC address for " + str(address) + "? ")

        if not bool(re.match(r'([A-Fa-f0-9]{2}:){5}([A-Fa-f0-9]{2})', answer)):
            print("Please enter the answer in the proper MAC address format.")
            continue

        if answer.upper() == mac:
            print("You are correct!")
            correctStatus = True
        elif answer.upper() != mac:
            print("You are incorrect.")
            correctStatus = False
        print("The MAC address for", address, "is", mac)

    return correctStatus


def main():
    # Select mode for game - Default: 0, ask on startup
    mode = 0
    # Select mode for game - Default: 0, ask on startup
    total = 0

    score = 0

    if mode == 0:
        mode = ChooseMode()
    if total == 0:
        total = ChooseTotal()
    for i in range(total):
        addresses = GenerateAddress(mode, mcastv4, mcastv6)
        for j in addresses:
            MACAddress = GenerateMAC(addresses[j])
            correctStatus = CheckAnswer(MACAddress, addresses[j])
            if correctStatus:
                score += 1

    print("Your score is", str(score), "out of", str(total) + ":", str(int((score / total) * 100)) + "%")


if __name__ == "__main__":
    main()

