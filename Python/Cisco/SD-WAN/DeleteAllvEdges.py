import requests
import urllib3
from getpass import getpass

# Disable certificate validation
urllib3.disable_warnings()


# Authenticate to vManage API
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


# Query for all valid vEdges and store them as vEdge objects
def queryEdges(apiObject, baseURL):
    edgeList = []
    queryURL = baseURL + "/system/device/vedges"
    response = apiObject.get(url=queryURL, verify=False)
    if response.status_code == 200:
        edgeDetailedList = response.json()["data"]
        for edge in edgeDetailedList:
            edgeList.append(edge["uuid"])
    return edgeList


# Invalidate the device certificate
def invalidateEdgeCertificate(apiObject, baseURL, edgeUUID):
    invalidateCertURL = baseURL + f"/certificate/{edgeUUID}"
    response = apiObject.delete(url=invalidateCertURL, verify=False)
    if response.status_code == 200:
        return True
    else:
        return False


# Delete vEdge Object
def deleteEdge(apiObject, baseURL, edgeUUID):
    edgeDeleteURL = baseURL + f"/system/device/{edgeUUID}"
    response = apiObject.delete(url=edgeDeleteURL, verify=False)
    if response.status_code == 200:
        print(f"Device {edgeUUID} has been deleted successfully!")
    else:
        print(f"Device {edgeUUID} has not been deleted. The following status code was returned: {response.status_code}")

    return response.status_code


# Main Function
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

    # Query for edge devices
    vEdgeList = queryEdges(vManageAPI, (baseURL + apiBasePath))

    # Invalidate the certificate for and delete all edge devices
    totalCount = len(vEdgeList)
    successfulCount = 0
    for uuid in vEdgeList:
        edgeDeleteStatus = deleteEdge(vManageAPI, (baseURL + apiBasePath), uuid)
        if edgeDeleteStatus == 200:
            successfulCount += 1

    print(f"Successfully deleted {successfulCount} out of {totalCount} vEdges!")


# Call main function
if __name__ == "__main__":
    main()
