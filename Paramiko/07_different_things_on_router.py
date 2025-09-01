# configure different things on each router
'''
In the previous script we have loop through the ip address list to connect to routers and configure the loopback1 on each router but there the ip address of loopback1 is same on each router.

In this script we will configure the ip address of loopback 2 on each router diffrent. The loopback address will be the last digit of the router ip address.
R1 ip - 10.10.10.1    loopback address - 10.6.1.1

'''

import paramiko
import time
import getpass

username = input("Enter the username: ")
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# List of routers ip address
ip_list = ["10.10.10.1", "10.10.10.2", "10.10.10.3", "10.10.10.4", "10.10.10.5"]

for ip in ip_list:
    router_id = ip.split(".")[-1]  # split the ip address of router and access the last element

    ssh_client.connect(hostname=ip, username=username, password=password)
    print("------------------------------------------------")
    print(f"Successfull login to {ip}")
    conn = ssh_client.invoke_shell() 

    # configure loopback2
    conn.send("conf t\n")
    conn.send("int lo2\n")                         
    conn.send(f"ip address 10.3.1.{router_id} 255.255.255.0\n")                         
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