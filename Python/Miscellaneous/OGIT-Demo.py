import urllib3
import requests
import json

urllib3.disable_warnings()

def changeDescription():
    url = "https://10.1.12.11/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1"
    payload = json.dumps({'Cisco-IOS-XE-native:GigabitEthernet': {'description': "More Cisco!!!"}})
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json',
        'Authorization': 'Basic bW9yZWNpc2NvOm1vcmVjaXNjbw=='
    }

    response = (requests.request("PATCH", url, headers=headers, data=payload, verify=False))
    return response


url = "https://10.1.12.11/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1"

payload={}
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic bW9yZWNpc2NvOm1vcmVjaXNjbw=='
}

response = (requests.request("GET", url, headers=headers, data=payload, verify=False)).json()
description = response['Cisco-IOS-XE-native:GigabitEthernet']['description']
print(response)
print(description)

print("--")

if description == "More Cisco!!!":
    print("You're good!!!")
elif description == "More Juniper!!!":
    print("This is a Cisco demo! Get outta here!")
    print(changeDescription())
else:
    print("This is not recognized! Let's change that!")
    print(changeDescription())