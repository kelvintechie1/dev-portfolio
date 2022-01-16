from Authenticate import DNAC
from Authenticate import authenticateToDNAC
from getpass import getpass

KB_DNAC = DNAC(input("Enter the username: "), getpass("Enter the password: "), "https://10.10.101.250")
token = authenticateToDNAC(KB_DNAC)

