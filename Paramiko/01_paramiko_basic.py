import paramiko
import time 
import getpass

ip_address = input("Enter IP_Address: ")
username = input("Enter Username: ")
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username, password=password)

print(f"Successfull login to {ip_address}")
conn = ssh_client.invoke_shell()

conn.send("conf t\n")
conn.send("int lo0\n")
conn.send("ip address 10.1.1.1 255.255.255.255")
time.sleep(1)

output = conn.recv(65535).decode()
print(output)

ssh_client.close()