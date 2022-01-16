import requests
import urllib3
from getpass import getpass

# Disable certificate warning
urllib3.disable_warnings()


# Authenticate and get CSRF token
def authenticateTovManage(baseURL, apiObject):
    username = input("Enter the username: ")
    password = getpass("Enter the password: ")
    body = {"j_username": username, "j_password": password}
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    response = apiObject.post(url=(baseURL + "/j_security_check"), headers=header, data=body, verify=False)

    jsessionid = (response.headers["Set-Cookie"]).split(";")
    return jsessionid[0]


# Get the API Token
def getAPIToken(baseURL, sessionID, apiObject):
    header = {"Cookie": sessionID}
    tokenURL = baseURL + "/dataservice/client/token"
    response = apiObject.get(url=tokenURL, headers=header, verify=False)
    if response.status_code == 200:
        return response.text
    else:
        return None


# Invalidate the device certificate
def invalidateEdgeCertificate(apiObject, baseURL, edgeUUID):
    invalidateCertURL = baseURL + "/certificate/device/invalidate"
    body = {"chassisNumber": edgeUUID}
    response = apiObject.delete(url=invalidateCertURL, verify=False)
    if response.status_code == 200:
        return True
    else:
        print(response.status_code)
        print(response.text)


def main():
    # Create list to store vEdges
    vManageAPI = requests.Session()
    baseURL = "https://10.5.255.112"
    apiBasePath = "/dataservice"

    # Authenticate to vManage and get the token
    sessionID = authenticateTovManage(baseURL, vManageAPI)
    token = getAPIToken(baseURL, sessionID, vManageAPI)

    # Set the session ID and token in the API session
    authHeaders = {"Cookie": sessionID, "X-XSRF-TOKEN": token}
    vManageAPI.headers = authHeaders
    vManageAPI.verify = False

    invalidateEdgeCertificate(vManageAPI, (baseURL + apiBasePath), "C8K-F01C1406-C76F-2B2B-891A-28F5B3A706E0")


# Call main function
if __name__ == "__main__":
    main()