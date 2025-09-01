# Configure the loopback address on multiple router at once and check network interfaces
'''
The script will configure the loopback0 on  multiple router R1, R2, R3, R4, R5 at once
R1 loopback0 10.10.10.1
R2 loopback0 10.10.10.2
R3 loopback0 10.10.10.3
R4 loopback0 10.10.10.4
R5 loopback0 10.10.10.5

Save the configuration

Also we are checking the network inteface of all the routers at once
'''

import paramiko
import time
import getpass

username = input("Enter Username: ") or "cisco"
passowrd = getpass.getpass() or "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for x in range(1,6):
    ssh_client.connect(hostname=f"10.10.10.{x}", username=username, password=passowrd)
    print("----------------------------------------------------------")
    print(f'Successfull Login to 10.10.10.{x}')
    conn = ssh_client.invoke_shell()

    # configure loopback0
    conn.send("conf t\n")
    conn.send("int lo0\n")
    conn.send(f"ip address 10.10.10.{x} 255.255.255.0\n")
    time.sleep(1)

    # save the configuration
    conn.send("do write\n")
    time.sleep(3)

    # check routers interface
    conn.send("do show interface brief | ex unas\n")          
    time.sleep(1)

    output = conn.recv(65535).decode()
    print(output)

    ssh_client.close()