# Remove the multiple loopback at once on the  single router
'''
The script will remove the loopback on router from loopback0 to loopback4 at once
'''

import paramiko
import time
import getpass

ip_address = input("Enter IP Addresss: ")
username = input("Enter Username: ")
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username, password=password)

print(f"Successfull Login to: {ip_address}")
conn = ssh_client.invoke_shell()

conn.send('conf t\n')

for n in range(5):
    conn.send(f"no interface lo{n}\n")
    time.sleep(0.5)

output = conn.recv(65535).decode()
print(output)

ssh_client.close()
