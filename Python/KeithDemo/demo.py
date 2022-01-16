import ipaddress as ip

class Router:
    def __init__(self, Name, IPAddress, Model, Version):
        self.Name = Name
        self.IPAddress = IPAddress
        self.Model = Model
        self.Version = Version

    def printAddress(self):
        print(self.IPAddress)

    def wipeConfiguration(self):
        # ALL THE CODE TO SSH IN AND GET ME FIRED BY WIPING THE CONFIG OF A PROD ROUTER
        print("Configuration wiped on", self.Name)

R1 = Router("R1", "192.168.1.1", "Cisco 2921", "15.4")
R2 = Router("R2", "192.168.1.2", "Cisco 2921", "15.4")
R3 = Router("R3", "192.168.1.3", "Cisco 2921", "15.3")

routerArray = [R1, R2, R3]
for router in routerArray:
    router.wipeConfiguration()

subnet1 = ip.IPv4Network("192.168.1.0/24")
print(type(subnet1))
for address in subnet1:
    print(type(address))
