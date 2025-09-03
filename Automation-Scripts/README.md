# Networking Automation Scripts

This section of the repository contains **Python scripts for network automation**.  
Each script is designed to simplify repetitive tasks in network configuration and management on Cisco devices.  
The goal is to save time, reduce manual errors, and make network administration more efficient.  

---

### 1. [dhcp_configuration.py](./dhcp_configuration.py)
This script automates the process of configuring **DHCP (Dynamic Host Configuration Protocol)** on Cisco routers.  
It connects to the device via SSH, applies DHCP pool configurations, sets default gateways, and assigns IP ranges automatically.  
The script ensures that devices in the network can receive IP addresses dynamically without manual configuration.  
Useful for **large-scale enterprise networks** where managing IP assignments manually would be time-consuming.  
Supports flexibility to modify **pool name, network range, and excluded addresses** based on user input.  

FLow of script:
When you start the script, it first asks you for the router’s management IP. Once you provide that, the script establishes an SSH session with that specific router. It then asks you for DHCP details such as pool name, network, subnet mask, and default gateway. Using those inputs, the script automatically generates the required Cisco IOS DHCP commands, sends them to the router, and saves the configuration. After finishing with one router, then loop through multiple routers if you extend it to configure the next one.


