# Create segment groups in NSX-T

from getpass import getpass
import urllib3 as ul
import requests
import json

# Disable whining about self-signed SSL certificates - but oh no, think of the PEOPLE!
ul.disable_warnings(ul.exceptions.InsecureRequestWarning)


class Segment:
    def __init__(self, segmentName, segmentType):
        self.segmentName = segmentName
        self.segmentType = segmentType

    def createSegmentGroups(self, user, pw, url):
        requestBody = {"expression": [{"member_type": "Segment", "value": f"segment|{self.segmentName}",
                                       "key": "Tag", "operator": "EQUALS", "resource_type": "Condition"}],
                       "description": f"{self.segmentName} {self.segmentType}",
                       "display_name": (f"{self.segmentName}-{self.segmentType}").upper()}
        requestHeaders = {"Content-Type": "application/json", "Accept": "application/json"}

        resp = requests.put(url=url, headers=requestHeaders, json=requestBody, auth=(user, pw), verify=False)

        if resp.status_code == 200 or 201:
            print(f"Successful creation of segment group for {self.segmentName} segment")
            return resp.json()
        else:
            print(f"Error in the creation of segment group for {self.segmentName} segment - unsuccessful.")
            return resp.status_code


def main():
    segmentList = [Segment("app", "prod"), Segment("web", "prod"), Segment("storage", "prod"), Segment("desktop", "prod")]
    username = input("Enter your NSX-T manager administrative username: ")
    password = getpass("Enter your NSX-T manager administrative password: ")
    policyAPIBaseURL = "https://ktc-vmwr-nsxm01.lab.trankelvin.com/policy/api/v1"
    for i in segmentList:
        creation = i.createSegmentGroups(username, password,
                                         (policyAPIBaseURL + f"/infra/domains/default/groups/{i.segmentName}-{i.segmentType}"))
        print(creation)


if __name__ == "__main__":
    main()
