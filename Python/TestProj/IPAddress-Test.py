import ipaddress

network = ipaddress.IPv4Network("67.83.1.64/27")
address = ipaddress.IPv4Address("67.83.1.95")

ips = list(network)

if address in ips:
    print("The address " + str(address) + " is in the network " + str(network))
else:
    print("The address " + str(address) + " is NOT in the network " + str(network))

foundIP = False

# for ip in ips:
#     if ip == address:
#         foundIP = True
#         print("The address " + str(address) + " is in the network " + str(network))
#         break
#
# if not foundIP:
#     print("The address " + str(address) + " is NOT in the network " + str(network))
