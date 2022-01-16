import requests
import urllib3

urllib3.disable_warnings()

reqHeaders = {"Accept": "application/yang-data+json", "Content-Type": "application/yang-data+xml"}
resp = (requests.get(url="https://sandbox-iosxe-recomm-1.cisco.com/restconf/data/ietf-yang-library:modules-state",
                     headers=reqHeaders, verify=False, auth=("developer", "C1sco12345"))).json()
for module in resp["ietf-yang-library:modules-state"]["module"]:
    print(module["name"])