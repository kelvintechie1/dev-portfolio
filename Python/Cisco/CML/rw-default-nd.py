# Script Purpose - modify Cisco Modeling Labs 2.x node definition files + cache for all default node definitions files to change read-only flag from True -> False
# Written by: Kelvin Tran (10/29/2020)
# Note: This script can easily be modified to make any other changes to the base config files instead of/in addition to making the NDs read/write.

# Directories containing default node definitions (assuming the copy-refplat-iso-to-disk.sh script has been run):
"""/var/lib/libvirt/images/node-definitions/
/var/local/virl2/refplat/diff/node-definitions/
/opt/refplat_images/node-definitions/"""
# Change in "directories" variable if your files are stored in other places (hint: use Linux "find" command to find YAML files)

# Import necessary libraries
import yaml # You may have to install PyYAML from the root user using the command "pip3 install --user pyyaml" - installing from sysadmin user fails unless sudo'd
import subprocess


def main():
    # Confirm that script is being run as root or a user with write-level permissions to the folders listed above
    print("Make sure this script is running as the root user (\"sudo /bin/bash\").")
    input("Press enter to confirm that this script is running as root. Otherwise, exit the script and re-run as root.")

    # Name of device scheme (w/out ".yaml") - default list commented down below
    #devices = ["alpine-trex", "alpine-wanem", "alpine", "asav", "coreos", "csr1000v", "desktop", "iosvl2", "iosv", "iosxrv9000", "iosxrv",
    #           "nxosv9000", "nxosv", "server", "ubuntu"]

    devices = ["csr1000v", "iosvl2", "iosxrv", "iosxrv9000", "nxosv", "nxosv9000"]

    # List of directories to read from/write to
    directories = ["/var/lib/libvirt/images/node-definitions/", "/var/local/virl2/refplat/diff/node-definitions/",
                  "/opt/refplat_images/node-definitions/"]

    # Directory to back-up original YAML files to
    backupDir = "/home/sysadmin/backupDir/"

    # Name of YAML files (device scheme + ".yaml")
    yamlNames = []
    for yamlItem in enumerate(devices):
        yamlNames.append(yamlItem[1] + ".yaml")

    for i in enumerate(directories):
        randomNumDir = backupDir + str(i[0])
        subprocess.call(["mkdir", "-p", randomNumDir])
        subprocess.call(["cp", "-Rf", i[1], randomNumDir])
        for j in yamlNames:
            try:
                with open((i[1] + j), 'r') as readFile:
                    temp = yaml.load(readFile, Loader=yaml.FullLoader)
                    print("Successfully read from file", (i[1] + j), "...")
            except FileNotFoundError as e:
                print(e)
                continue

            config = temp["configuration"]["provisioning"]["files"]

            for count in enumerate(config):
                 config[count[0]]["content"] = ''

            with open((i[1] + j), 'w') as writeFile:
                yaml.dump(temp, writeFile)
                print("Successfully written to file", (i[1] + j), "...")


def ChangeOthers():
    # Name of device scheme (w/out ".yaml")
    devices = ["unmanaged_switch", "external_connector", "server"]
    # Directory containing the files
    directory = ["/var/local/virl2/.local/lib/python3.6/site-packages/simple_core/sample/"]
    # Directory to back-up original YAML files to
    backupDir = "/home/sysadmin/backupDir/ChangeOthers"
    # Name of YAML files (device scheme + ".yaml")
    yamlNames = []
    for yamlItem in enumerate(devices):
        yamlNames.append(yamlItem[1] + ".yaml")

    for i in enumerate(directory):
        subprocess.call(["mkdir", "-p", backupDir])
        for j in yamlNames:
            subprocess.call(["cp", "-Rf", (i[1] + j), backupDir])
            try:
                with open((i[1] + j), 'r') as readFile:
                    temp = yaml.load(readFile, Loader=yaml.FullLoader)
                    print("Successfully read from file", (i[1] + j), "...")
            except FileNotFoundError as e:
                print(e)
                continue

            temp["general"]["read_only"] = False

            with open((i[1] + j), 'w') as writeFile:
                yaml.dump(temp, writeFile)
                print("Successfully written to file", (i[1] + j), "...")


if __name__ == "__main__":
    # Make modifications to main nodes (i.e. IOSv, CSR1000v, IOS XRv 9000, etc.) - Comment out if you don't want this.
    main()

    # Note that the Server, Unmanaged Switch, and External Connector nodes remain unchanged with this script by default.
    # Uncomment the following line if you want those changed as well:
    #ChangeOthers()

    print("Make sure to restart your CML2 controller for these changes to take effect. Run \"shutdown -r now\" at the CLI to restart immediately.")
