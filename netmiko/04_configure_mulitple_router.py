## Looping to configure interface in all routers at once 
"""
We have 5 routers in our toplopgy having ip addresses 
r1 10.10.10.1
r2 10.10.10.2
r3 10.10.10.3
r4 10.10.10.4
r5 10.10.10.5
Create loopback interface on each router 

"""

from netmiko import ConnectHandler

for n in range(1,6):
    r = {
        'device_type':'cisco_ios',
        'host': f'10.10.10.{n}',
        'username':'cisco',
        'password':'cisco'
    }

    # Establish SSH coonection 
    conn = ConnectHandler(**r)

    # Configuration Changes commands
    config_commands = {
        'int lo0'
        f'ip address 10.1.1.{n} 255.255.255.255'
        'int lo1'
        f"ip address 10.2.2.{n} 255.255.255.255"

    }

    # Send the configurations commands
    output = conn.send_config_set(config_commands)
    print('---------------------------------')
    print(output)

    # Send the command to see interface brief
    output = conn.send_command("show ip interface brief | exclude unassign ")
    print(output)
