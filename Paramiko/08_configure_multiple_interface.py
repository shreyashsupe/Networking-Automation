# The script will be used to configure multiple interface on each router i.e we will use nested looping

"""
The script will be used to configure mulitple loopback addresses on multiple routers 
Routers ip - ["10.10.10.1", "10.10.10.2", "10.10.10.3", "10.10.10.4", "10.10.10.5"]
We will configure loopback address from loopback3 to loopback6 
lo3 10.4.1.{router_id}
lo4 10.5.1.{router_id}
lo5 10.6.1.{router_id}
lo6 10.7.1.{router_id}
"""
import paramiko
import time 
import getpass

username = input("Enter username: ")
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

    # Enter configuration mode
    conn.send("conf t\n")

    # configure multiple loopback addresses
    for x in range(3,7):
        conn.send(f"int lo{x}\n")               
        conn.send(f"ip address 10.{x+1}.1.{router_id} 255.255.255.0\n")                         
        time.sleep(1)

    # save the configurations
    conn.send("do write\n")
    time.sleep(3)

    # Check router interface
    conn.send("do show interface brief\n")
    time.sleep(1)

    # Print the output
    output = conn.recv(65535).decode()  
    print(output)

    ssh_client.close()
