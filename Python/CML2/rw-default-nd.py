# Script Purpose - modify Cisco Modeling Labs 2.x node definition files + cache for all default node definitions files to change read-only flag from True -> False
# Written by: Kelvin Tran (10/29/2020)

# Directories containing default node definitions (assuming the copy-refplat-iso-to-disk.sh script has been run):
"""/var/lib/libvirt/images/node-definitions/
/var/local/virl2/refplat/diff/node-definitions/
/opt/refplat_images/node-definitions/"""
# Change in "directories" variable if your files are stored in other places (hint: use Linux "find" command to find YAML files)

# Import necessary libraries
import yaml
import subprocess


def main():

    # Confirm that script is being run as root
    print("Make sure this script is running as the root user (\"sudo /bin/bash\").")
    input("Press enter to confirm that this script is running as root. Otherwise, exit the script and re-run as root.")

    # Name of device scheme (w/out ".yaml")
    devices = ["alpine-trex", "alpine-wanem", "alpine", "asav", "coreos", "csr1000v", "desktop", "iosvl2", "iosv", "iosxrv9000", "iosxrv",
               "nxosv9000", "nxosv", "server", "ubuntu"]

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

            temp["general"]["read_only"] = False

            with open((i[1] + j), 'w') as writeFile:
                yaml.dump(temp, writeFile)
                print("Successfully written to file", (i[1] + j), "...")


if __name__ == "__main__":
    main()
    print("Make sure to restart your CML2 controller for these changes to take effect. Run \"shutdown -r now\" at the CLI to restart immediately.")

