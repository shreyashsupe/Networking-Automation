## Secure VPC Setup with EC2 

**Project**
- Design and configure a VPC: Create a VPC with custom IP ranges. Set up public and private subnets. Configure route tables and associate subnets.

- Implement network security: Set up network access control lists (ACLs) to control inbound and outbound traffic. Configure security groups for EC2 instances to allow specific ports and protocols.

- Provision EC2 instances: Launch EC2 instances in both the public and private subnets. Configure security groups for the instances to allow necessary traffic. Create and assign IAM roles to the instances with appropriate permissions.

- Networking and routing: Set up an internet gateway to allow internet access for instances in the public subnet. Configure NAT gateway or NAT instance to enable outbound internet access for instances in the private subnet. Create appropriate route tables and associate them with the subnets.

- SSH key pair and access control: Generate an SSH key pair and securely store the private key. Configure the instances to allow SSH access only with the generated key pair. Implement IAM policies and roles to control access and permissions to AWS resources.

- Test and validate the setup: SSH into the EC2 instances using the private key and verify connectivity. Test network connectivity between instances in different subnets. Validate security group rules and network ACL settings.


**What was Done**

- Created a VPC with custom CIDR and multiple subnets (public + private in 2 AZs).

- Configured route tables, Internet Gateway, and NAT Gateways for internet access.

- Set up Security Groups and NACLs to control traffic.

- Launched EC2 instances in private subnets using an Auto Scaling Group.

- Created a Bastion Host in public subnet for secure SSH access to private EC2s.

- Installed a Python HTTP server on EC2 instances (port 8000).

- Deployed an Application Load Balancer in public subnets to distribute traffic.

- Verified connectivity, scaling, and security rules.


```
                   Internet
                       |
               +----------------+
               |  Load Balancer |
               +----------------+
                /              \
         Public Subnet       Public Subnet
           (AZ-1)              (AZ-2)
           |   |               |   |
     NAT GW   Bastion     NAT GW   Bastion
           \    |             |    /
   ---------------- VPC ----------------
   |                                     |
   |   Private Subnet (AZ-1)             |
   |   +-----------------------------+   |
   |   |  EC2 Instances (Auto Scale) |   |
   |   +-----------------------------+   |
   |                                     |
   |   Private Subnet (AZ-2)             |
   |   +-----------------------------+   |
   |   |  EC2 Instances (Auto Scale) |   |
   |   +-----------------------------+   |
   ---------------------------------------


```