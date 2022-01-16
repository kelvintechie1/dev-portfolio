import requests
import json
import virl2_client
import time
import sys
import subprocess
from getpass import getpass


def GetAuth():
    user = input("Enter your vCenter username. ")
    password = getpass("Enter your vCenter password. ")

    return [user, password]


def GetToken(request, url):
    data = request.get(url=(url + "rest/com/vmware/cis/session"))
    jsonData = json.load(data)
    print(jsonData)


def main():
    credentials = GetAuth()

    tokenRequest = requests.Session()
    tokenRequest.auth(credentials[0], credentials[1])
    tokenRequest.headers.update({'Accept': 'application/vnd.vmware.vmw.rest-v1+json',
                                 'Content-Type': 'application/vnd.vmware.vmw.rest-v1+json'})

    url = "https://ktl-vmwr-vc01.ad.trankelvin.com/"

    GetToken(tokenRequest, url)


if __name__ == "__main__":
    main()