# Script to remote mutiple routers and run show command on each router at once 
"""
We have 5 routers in our toplopgy having ip addresses 
r1 10.10.10.1
r2 10.10.10.2
r3 10.10.10.3
r4 10.10.10.4
r5 10.10.10.5
We have to loop through all this routers and execute 'show ip interface brief' command  on each router at once
"""

from netmiko import ConnectHandler

for n in range(1,6):
    r = {
        'device_type':'cisco_ios',
        'host': f'10.10.10.{n}',
        'username':'cisco',
        'password':'cisco'
    }

    # Establish an SSH connection
    conn = ConnectHandler(**r)

    # Send the command 
    output = conn.send_command('show ip interface brief | exclude unassign ')
    print("------------------------------------------------")
    print(f"Inteface for router {r['host']}")
    print(output)

