# This script automates DHCP pool configuration on multiple Cisco routers via SSH.
# It prompts the user for router credentials and VLAN DHCP details, then applies the settings.
# Uses Netmiko to connect, configure, save, and disconnect from each router automatically.


from netmiko import ConnectHandler


def configure_dhcp_on_router(router_params, vlan_configs):
    """
    router_params: Dictionary conataining router connections details(IP, username, password, device type, enable secret).
    vlan_configs: List of dictionaries, each describing VLAN DHCP pool details.
    """
    try:
        net_connect = ConnectHandler(**router_params)           # create a SSH connection to the router 
        net_connect.enable()                                    # Enter enable mode


        commands = []          # Empty list to store commands to configure DHCP pools
        # loop through each vlan configuration
        for vlan in vlan_configs:
            pool_name = f"VLAN{vlan['vlan']}"
            commands.extend([
                f"IP dhcp pool {pool_name}",
                f"network {vlan['network']} {vlan['mask']}",
                f"default router {vlan['default_router']}",
                f"dns-server {vlan['dns_server']}",
                "exit"
            ])

        output = net_connect.send_config_set(commands)         # send entire set of command to the router in configuration mode 
        print(f"Configurtion output for {router_params['host']}:\n{output}")  

        net_connect.save_config()     # save the configuration 
        net_connect.disconnect()      # disconnect the SSH session

    except Exception as e:
        print(f"Failed to configure router {router_params['host']}: {e}")


# Function to prompt user to enter connections details for router
def get_router_info():
    router = {}
    router['device_type'] = 'cisco_ios'
    router['host'] = input("Enter router IP/hostname: ")
    router['username'] = input("Enter username: ")
    router['password'] = input("Enter password: ")
    router['secret'] = input("Enter enable secret (if none, press enter): ") or ''
    return router

# Function to prompt user to enter teh details to create DHCP pool for VLAN
def get_vlan_info():
    vlan = {}
    vlan['vlan'] = input("Enter VLAN ID (eg. 10): ")
    vlan['network'] = input("Enter network address (eg. 192.168.10.0): ")
    vlan['mask'] = input("Enter subnet mask (Eg. 255.255.255.0): ")
    vlan['default_router'] = input("Enter default router IP (eg. 192.168.10.1): ")
    vlan['dns_server'] = input("Enter DNS server IP (eg. 8.8.8.8): ")
    return vlan 


if __name__ == "__main__":
    """
    ask for number of routers to configure
    loop over the number of routers user enters 
        for each router, calls get_router_info() to get connection details 
        ask for the number of VLAN to configure on this router
        loops for each VLAN, calls get_vlan_info() to get DHCP pool details and appends to vlan_configs
        calls configure_dhcp_on-routers() to connect and sedn commands to the router
    Prints a completion message 
    """
    num_routers = int(input("Enter the number of routers to configure: "))
    for r in range(num_routers):
        print(f"\nRouter {r+1} configuration: ")
        router_params = get_router_info()

        num_vlan = int(input("Enter the number of VLAN to configure on this router: "))
        vlan_configs = []
        for v in range(num_vlan):
            print(f"VLAN {v +1} details: ")
            vlan_configs.append(get_vlan_info())

        print(f"\nConfiguring router {router_params['host']} ...")
        configure_dhcp_on_router(router_params, vlan_configs)

    print(f"\nAll routers configured.")
