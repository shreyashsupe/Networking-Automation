# Company/Business System Network Design (Cisco Packet Tracer)

## Project Overview
This project demonstrates the design and implementation of a **hierarchical company network** using **Cisco Packet Tracer**.  
The network is designed for a trading floor support center to ensure **reliability, scalability, security, and redundancy**.  

The design follows the **three-layer hierarchical model**:
- **Core Layer** – Redundant routers with OSPF and PAT
- **Distribution Layer** – Multilayer switches handling inter-VLAN routing
- **Access Layer** – Departmental switches with VLAN segmentation and port-security

## Objectives
- Build a **hierarchical network** with redundancy (dual core routers, multilayer switches, dual ISPs)  
- Create **departmental VLANs** and subnets  
- Configure **OSPF (dynamic routing)** + static routes  
- Implement **SSH** for secure device management  
- Enable **DHCP for dynamic addressing** and static IP for servers  
- Apply **NAT/PAT** for internet access  
- Enforce **security measures** (ACLs, port-security)  
- Verify connectivity with **ping, traceroute, and show commands**  

---

## Network Topology
The network includes:
- **Core Layer:** 2 Routers (CORE-R1, CORE-R2)  
- **Distribution Layer:** 2 Multilayer Switches (Mlt-SW1, Mlt-SW2)  
- **Access Layer:** 6 Departmental Switches (Sales, HR, Finance, Admin, ICT, Server Room)  
- **ISPs:** ISP-1 and ISP-2 (configured only with interfaces + OSPF)  
- **End Devices:** PCs, DHCP Server, DNS Server, HTTP Server, Wireless APs  

---

## IP Addressing Scheme
- **Sales & Marketing (VLAN 10):** 192.168.10.0/24  
- **HR & Logistic (VLAN 20):** 192.168.20.0/24  
- **Finance & Accounts (VLAN 30):** 192.168.30.0/24  
- **Admin & Public (VLAN 40):** 192.168.40.0/24  
- **ICT (VLAN 50):** 192.168.50.0/24  
- **Server Room (VLAN 60):** 192.168.60.0/24  
- **Core-to-Core Links:** 10.10.10.x/30  
- **Core-to-ISP Links:** 103.133.254.x/30  

---

## Configuration Steps
1. **Basic Settings** – Hostname, banner, passwords, SSH enabled on all routers & switches  
2. **VLANs** – Created VLANs for each department + trunk/access ports assigned  
3. **Port Security** – Applied to Finance department (1 MAC per port, sticky, violation shutdown)  
4. **Subnetting & IP Addressing** – Assigned subnets and configured interfaces  
5. **OSPF (Process ID 10)** – Configured on routers & multilayer switches  
6. **Static IPs** – Assigned to Server Room devices  
7. **DHCP** – Configured on server to provide dynamic IPs to clients  
8. **Inter-VLAN Routing** – Implemented on multilayer switches with `ip helper-address`  
9. **Wireless Configurations** – Access Points for each department  
10. **NAT/PAT & ACL** – Configured on core routers for internet access and filtering  
11. **Default Static Routes** – Configured for redundancy (primary + backup)  
12. **Verification** – Using `ping`, `traceroute`, `show` commands  

---

## Sample Commands

### 🔹 Access Layer (Sales Switch)
```bash
hostname Sales-SW
vlan 10
name Sales
int range fa0/3-24
 switchport mode access
 switchport access vlan 10
int range fa0/1-2
 switchport mode trunk


### 🔹 Distribution Layer (Finance Switch – Port Security)
```bash
int range fa0/3-24
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
