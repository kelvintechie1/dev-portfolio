import subprocess

i = 0
while True:
    subprocess.call(["ping", "ddos.networkchuck.com", "-c", "1", "-i", "1"])
    i += 1
    print(i)