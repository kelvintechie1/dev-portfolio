# Create segment groups in NSX-T

from getpass import getpass
import urllib3 as ul
import requests
import json

# Disable whining about self-signed SSL certificates - but oh no, think of the PEOPLE!
ul.disable_warnings(ul.exceptions.InsecureRequestWarning)


# Define object class for NSX-T segment
class Segment:
    def __init__(self, segmentName, segmentType):
        self.segmentName = segmentName
        self.segmentType = segmentType

    def createSegmentGroups(self, user, pw, url):
        # Form HTTP request body and request headers for API call
        requestBody = {"expression": [{"member_type": "Segment", "value": f"segment|{self.segmentName}",
                                       "key": "Tag", "operator": "EQUALS", "resource_type": "Condition"}],
                       "description": f"{self.segmentName} {self.segmentType}",
                       "display_name": (f"{self.segmentName}-{self.segmentType}").upper()}
        requestHeaders = {"Content-Type": "application/json", "Accept": "application/json"}

        # Send PUT to NSX-T policy controller to create sgement group
        resp = requests.put(url=url, headers=requestHeaders, json=requestBody, auth=(user, pw), verify=False)

        # Test whether status code indicates successful request; return response if yes, return error code if no
        if resp.status_code == 200 or 201:
            print(f"Successful creation of segment group for {self.segmentName} segment")
            return resp.json()
        else:
            print(f"Error in the creation of segment group for {self.segmentName} segment - unsuccessful.")
            return resp.status_code


def main():
    # Define list of segments for NSX to create groups for
    segmentList = [Segment("app", "prod"), Segment("web", "prod"), Segment("storage", "prod"), Segment("desktop", "prod")]

    # Ask for credentials and store in username/pw variable for use in API calls
    username = input("Enter your NSX-T manager administrative username: ")
    password = getpass("Enter your NSX-T manager administrative password: ")

    # Define base URL for the NSX-T Policy API
    policyAPIBaseURL = "https://ktc-vmwr-nsxm01.lab.trankelvin.com/policy/api/v1"

    # Loop through segments in segment list and run createSegmentGroup method to run API call to create segment group
    for i in segmentList:
        creation = i.createSegmentGroups(username, password,
                                         (policyAPIBaseURL + f"/infra/domains/default/groups/{i.segmentName}-{i.segmentType}"))
        print(creation)  # Print either JSON from request (200/201) or HTTP status code (any other code - error)


# Run main module only if script not being imported externally
if __name__ == "__main__":
    main()
