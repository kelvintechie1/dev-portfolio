#!/usr/local/bin/python3.9

# Import needed libraries
import mrtparse
import sys


def loadFile(filePath):
    routes = []
    index = 0
    desiredIndex = 10
    endIndex = 100
    for entry in mrtparse.Reader(filePath):
        if index < desiredIndex:
            index += 1
            continue
        routes.append(entry.data)
        index += 1
        if index == endIndex:
            break
    return routes


def main():
    path = "/Users/kelvintran/Desktop/bview.20190131.1600.gz"
    bgpRoutes = loadFile(path)
    for routes in bgpRoutes:
        if routes['subtype'][1] == "RIB_IPV4_UNICAST":
            print(routes['prefix'] + "/" + str(routes["prefix_length"]))


if __name__ == "__main__":
    main()
