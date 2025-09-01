# Configure multiple routers at once using looping and list
"""
Loop thorugh the list of ip address of router to establish ssh connection and send show command to each of them. Best practise if we have differnet ip address format. 
"""

from netmiko import ConnectHandler

ip_list = ['10.10.10.1', '10.10.10.2', '10.10.10.3', '10.10.10.4', '10.10.10.5']

for ip in ip_list:
    r = {
        'device_type':'cisco_ios',
        'host': ip,
        'username':'cisco',
        'password':'cisco'
    }

    # Establish SSH coonection 
    conn = ConnectHandler(**r)

    # Send the command to see interface brief
    output = conn.send_command("show ip interface brief | exclude unassign ")
    print('---------------------------------')
    print(output)