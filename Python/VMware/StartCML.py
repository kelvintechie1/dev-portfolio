# Get list of VMs

# Import necessary libraries
import ipaddress
import os
import requests
import subprocess
import sys
import time


def StartVMRest(listen_ip, listen_port):
    print(str(listen_ip) + " = IP Address / " + str(listen_port) + " = port number")
    subprocess.Popen(['vmrest', '-p', str(listen_port), '-i', str(listen_ip)])

    return


def StopVMRest():
    os.system("pkill \"(.*)vmrest(.*)\"")


def GetVMList(baseurl, request):
    vm = request.get(str(baseurl) + '/vms')
    data = vm.json()

    for iterations, vms in enumerate(data):
        if "CML" in str(vms['path']):
            id = vms['id']
            path = vms['path']
            break

    return id


def StartCMLVM(id, baseurl, request):
    powerOn = request.put((baseurl + '/vms/' + str(id) + '/power'), 'on')
    powerOn = powerOn.json()

    success = False
    if powerOn['power_state'] == 'poweredOn':
        success = True
    else:
        print("Failure to turn on VM. The program will now attempt to turn off the VM and exit.")
        request.put((baseurl + '/vms/' + str(id) + '/power'), 'off')
        sys.exit("Failure to turn on VM. VM has been turned off for safety.")
    return success


def askParameters():
    ip = input("Enter the listening IPv4 address of the vmrest service. Leave blank for default (127.0.0.1). ")
    port = input("Enter the listening port of the vmrest service. Leave blank for default (port 8697). ")
    secure = input("Enter http if you are using HTTP and https if you're using HTTPS. Leave blank for default (http)")

    # Replace with defaults if blank
    if (ip == ""):
        ip = ipaddress.IPv4Address("127.0.0.1")
    if (port == ""):
        port = int(8697)
    if (secure == ""):
        secure = bool(False)

    if (ip != "127.0.0.1"):
        try:
            ip = ipaddress.IPv4Address(ip)
        except (ipaddress.AddressValueError, TypeError):
            print("Invalid IP address. Try again.")
            ip = None
            port = None
            sys.exit("Invalid IP address.")

    if (port != "8697"):
        try:
            port = int(port)
        except (ValueError, TypeError):
            print("Invalid port number. Try again.")
            ip = None
            port = None
            sys.exit("Invalid port number.")

    if (secure != bool(False)):
        if (secure.lower() == "http"):
            secure = bool(False)
        elif (secure.lower() == "https"):
            secure = bool(True)
        else:
            print("Invalid entry. Please try again. Program exiting.")
            sys.exit("Invalid entry for secure status.")

    return [secure, ip, port]


def LaunchChrome(name):
    os.system("open -a /Applications/Google\ Chrome.app https://" + name)
    return True


# Create requests session object
request = requests.Session()
request.auth = ('kelvintran', 'VMware0405!')
request.headers.update(
    {'Accept': 'application/vnd.vmware.vmw.rest-v1+json', 'Content-Type': 'application/vnd.vmware.vmw.rest-v1+json'})

params = askParameters()
baseurl = ""
if params[0] == False:
    baseurl += "http://"
elif params[0] == True:
    baseurl += "https://"
baseurl += str(params[1]) + ":"
baseurl += str(params[2]) + "/api"

StartVMRest(params[1], params[2])
time.sleep(5)  # Wait 5 seconds to ensure that the vmrest service is properly started.

CML = GetVMList(baseurl, request)
StartVM = StartCMLVM(CML, baseurl, request)
if StartVM == True:
    print("Cisco Modeling Labs (CML) VM has successfully been started with ID " + str(CML))

resourceLocator = "cml"
launchBrowser = LaunchChrome(resourceLocator)
if launchBrowser == True:
    print("Chrome has been successfully opened with a new tab for the CML console at https://" + resourceLocator)
