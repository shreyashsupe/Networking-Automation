# Script to create a loopback interface on the router 

from netmiko import ConnectHandler

r1 = {
    'device_type' : 'cisco_ios',
    'host':'10.10.10.1',
    'username':'cisco',
    'password':'cisco'
}

conn = ConnectHandler(**r1)

# Execute configuration change commands (will automatically enter into config mode and end it also)
config_commands = {
    'int lo0'
    'ip address 10.1.1.1 255.255.255.255'
    'int lo1'
    'ip address 10.1.1.2 255.255.255.255'        # Created two loopback interfaces 0 and 1
}

# send the configuration commands 
output = conn.send_config_set(config_commands)
print(output)


# Execute show command to check loopback address are created or not
output = conn.send_command("show ip interface brief")
print(f"Interfaces for router {r1['host']}")
print(output)

