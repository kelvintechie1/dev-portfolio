# Import device class & other dependencies
from Device import Device
import requests
import urllib3
from getpass import getpass
import json


# Change hostname
def changeHostname(deviceObject):
    desiredHost = deviceObject.host
    print(f"Changing device name to {desiredHost}")
    requestBody = json.dumps({"Cisco-IOS-XE-native:native": {"hostname": desiredHost}})
    requestHeader = {"Accept": "application/yang-data+json",
                     "Content-Type": "application/yang-data+json"}
    # Check if hostname is already there
    resp = (requests.get(url=f"https://{deviceObject.address}/restconf/data/Cisco-IOS-XE-native:native/hostname",
                         headers=requestHeader, auth=(deviceObject.user, deviceObject.pw), verify=False))
    if resp.status_code == 200:
        if (existingHost := resp.json()["Cisco-IOS-XE-native:hostname"]) == desiredHost:
            print("Hostname already matches")
            return True
    else:
        return resp.status_code
    # Commit request
    resp = requests.patch(url=f"https://{deviceObject.address}/restconf/data/Cisco-IOS-XE-native:native",
                          data=requestBody, headers=requestHeader, auth=(deviceObject.user, deviceObject.pw), verify=False)
    print(resp.status_code)
    try:
        return resp.json()
    except json.decoder.JSONDecodeError:
        return True


def main():
    # Disable HTTP Insecure Warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # Get credentials
    user = input("Enter user: ")
    pw = getpass("Enter pass: ")
    # Create devices
    R1 = Device("KTL-CSCO-C8K01", "172.16.0.35", user, pw)
    R2 = Device("KTL-CSCO-C8K02", "172.16.0.36", user, pw)
    R3 = Device("KTL-CSCO-C8K03", "172.16.0.37", user, pw)
    allDevices = {R1, R2, R3}

    for device in allDevices:
        print(changeHostname(device))


if __name__ == "__main__":
    main()