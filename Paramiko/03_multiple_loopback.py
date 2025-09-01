# Creating multiple loopback address on a single router at once
'''
The script will configure the loopback addresses from 0 to 4 on single router at once 
loopback 0 - 10.10.10.1
loopback 1 - 10.10.10.2
loopback 2 - 10.10.10.3
loopback 3 - 10.10.10.4
loopback 4 - 10.10.10.5
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

for n in range(0,5):
    conn.send(f"int lo{n}\n")
    conn.send(f"ip address 10.10.10.{n+1} 255.255.255.255\n")
    time.sleep(1)

output = conn.recv(65535).decode()
print(output)

ssh_client.close()

