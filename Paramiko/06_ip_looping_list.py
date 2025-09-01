# Looping through ip address using a list
'''
The script will loop through the list of ip addresses creating the loopback1 in each router haivng the ip address 10.5.1.1
i.e each router will have the loopback1 having ip address 10.5.1.1 
We have 5 routers having ip addresses 
R1 - 10.10.10.1
R2 - 10.10.10.2
R3 - 10.10.10.3
R4 - 10.10.10.4
R5 - 10.10.10.5

'''

import paramiko
import time
import getpass

username = input("Enter ther username: ")
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# List of routers ip addresses 
ip_list = ["10.10.10.1", "10.10.10.2", "10.10.10.3", "10.10.10.4", "10.10.10.5"]

for ip in ip_list:
    ssh_client.connect(hostname=ip, username=username, password=password)
    print("------------------------------------------------")
    print(f"Successfull login to {ip}")
    conn = ssh_client.invoke_shell()

    # configure loopback1 
    conn.send("conf t\n")
    conn.send("int lo1\n")                         
    conn.send("ip address 10.2.1.1 255.255.255.0\n")                         
    time.sleep(1)

    # save the configurations
    conn.send("do write\n")
    time.sleep(3)

    # Check router interface
    conn.send("do show interface brief\n")
    time.sleep(1)

    output = conn.recv(65535).decode()
    print(output)

    ssh_client.close()

