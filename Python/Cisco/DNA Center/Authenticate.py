# Authenticate to DNA Center and get token
import base64
import requests
import urllib3

urllib3.disable_warnings()


class DNAC:
    def __init__(self, username, password, baseURL):
        self.username = username
        self.password = password
        self.baseURL = baseURL


def authenticateToDNAC(DNACObject):
    url = DNACObject.baseURL + "/dna/system/api/v1/auth/token"
    username = DNACObject.username
    password = DNACObject.password
    requestHeaders = {"Content-Type": "application/json", "Accept": "application/json"}
    response = (requests.post(url=url, auth=(username, password), headers=requestHeaders, verify=False)).json()
    token = response["Token"]

    return token

def main():
    print("Placeholder")


if __name__ == "__main__":
    main()