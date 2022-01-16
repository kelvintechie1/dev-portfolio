# Import device class & other dependencies
from Device import Device
import requests
import urllib3
from getpass import getpass
import json
import re

# Set loopback address of Loopback0 within 192.168.254.R/24 range
def setLoopback(deviceObject):
    loopbackIP = deviceObject.mgmtLoopbackIP
    loopbackInt = re.findall("[0-9]+$", deviceObject.mgmtLoopback)[0]
    print(f"Configuring IP address of Loopback{loopbackInt} to {loopbackIP}.")

    requestHeaders = {"Accept": "application/yang-data+json", "Content-Type": "application/yang-data+json"}
    requestBody = json.dumps({"Cisco-IOS-XE-native:native": {"interface": {"Loopback":
                [{"name": loopbackInt, "ip": {"address": {"primary": {"address": loopbackIP, "mask": "255.255.255.255"}}}}]}}})
    resp = requests.patch(url=f"https://{deviceObject.address}/restconf/data/Cisco-IOS-XE-native:native", data=requestBody,
                        auth=(deviceObject.user, deviceObject.pw), headers=requestHeaders, verify=False)
    try:
        if resp.status_code == 200 or 204:
            print(f"Interface Loopback IP changed to {loopbackIP} on Loopback{loopbackInt}")
            return resp.json()
        else:
            print(f"An error has occurred. Status code {resp.status_code}")
    except json.decoder.JSONDecodeError:
        return resp.text


def main():
    # Disable HTTP Insecure Warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # Get credentials
    user = input("Enter user: ")
    pw = getpass("Enter pass: ")
    # Create devices
    R1 = Device("KTL-CSCO-C8K01", "172.16.0.35", user, pw, mgmtLoopback="Loopback3525", mgmtLoopbackIP="192.168.254.1")
    R2 = Device("KTL-CSCO-C8K02", "172.16.0.36", user, pw, mgmtLoopbackIP="192.168.254.2")
    R3 = Device("KTL-CSCO-C8K03", "172.16.0.37", user, pw, mgmtLoopbackIP="192.168.254.3")
    allDevices = {R1, R2, R3}

    for device in allDevices:
        print(setLoopback(device))


if __name__ == "__main__":
    main()