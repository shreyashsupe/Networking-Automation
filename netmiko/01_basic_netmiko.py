from netmiko import ConnectHandler

# Directory representing the device
r1 = {
    'device_type':'cisco_ios',
    'host':'10.10.10.1',
    'username':'cisco',
    'password':'cisco'
}

# Establish an SSH connection to the device by passing in the device dictionary.
conn = ConnectHandler(**r1)

# Execute show command on router
output = conn.send_command("show ip interface brief")
print(f"Interfaces for router {r1['host']}")
print(output)