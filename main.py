# Author : B3TA-BLOCKER
# Github: https://github.com/B3TA-BLOCKER


#!/usr/bin/python 

# impoting the required  moudles
import os
import subprocess
import psutil  # provides an easy way to interact with system and process utilities

# The function automates running shell commands and retrieving their output as a cleaned-up string.
def bash(command) ->str :

    try:
        return subprocess.check_output(command, shell=True).decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e.output.decode('utf-8')}")
        raise


def network_interface_info() ->str :

    """Returns the name of the Network interface to be used."""
    # Get the network interfaces and their statuses
    interfaces = psutil.net_if_stats()
    list_of_interfaces_running = [] # An empty list to store the names of the running interfaces.

    # Iterate through the interfaces and check which ones are up
    for interface, stats in interfaces.items():
        if stats.isup: # if the interfface is up and running it will be appended in the list "list_of_interfaces_running"
            list_of_interfaces_running.append(interface)
    
    iterations = len(list_of_interfaces_running)
    
    while True:
            # Give choice to the user to chose the desire running network interface
            print("\nList of Running Interfaces:\n")
            for i in range(iterations):
                print(f"{i+1}. {list_of_interfaces_running[i]}")
            try:
                print("\nChoose One of the foillowing Network Interface :")
                choice = int(input("-> "))
                
                if choice > iterations or choice < 1:
                    os.system('clear')
                    print("Wrong Entry Try Again !!!! ")
                else:
                    break   
            except ValueError:
                # Handle the case where the input is not an integer
                os.system('clear')
                print("Invalid input. Please enter an integer.")
    return list_of_interfaces_running[choice - 1]


def get_local_network_info() ->str :

    """Returns the Local Subnet"""
    interface = network_interface_info()
    local_ip = bash(command=f"ifconfig {interface} | grep -A 1 'inet ' | awk '$1 == \"inet\" {{print $2}}'")
    subnet = '.'.join(local_ip.split('.')[:-1]) + '.0/24'
    return subnet


def nmap(ip):

    """Scans The TCP ports of the Target IP"""
    print(f"\nScanning TCP ports on {ip}\n" )
    result = bash(f"nmap -T4 -p1-65535 {ip} | grep 'open'").splitlines()
    ports = [] # Empty list for storing open ports

    for port in result:
        print(port)
        ports.append(port.split("/")[0])
    
    port_list = ",".join(ports)
    print("\nRunning Intence Scan on Open Ports .... \n")
    bash(f"nmap -T4 -A -sV -p{port_list} -oN output.txt {ip}")
    print(f"Nmap intence scan results logged in output.txt")
    exit()


# Clear screen 
os.system('clear')
subnet =  get_local_network_info()

os.system('clear')
print(f"\nRunning NetDiscover on local subnet : {subnet}\n")
ips = bash(f"sudo netdiscover -P -r {subnet} | grep '1' | cut -d ' ' -f2 ").splitlines()


# Taking the user input for the target ip
while True:
    print("List of IPs Discovered:\n")
    for i in range(0,len(ips)):
        if i == 0 :
            print(f"{i} - Exit")
        ip = ips[i]
        print(f"{i+1} - {ip}")
    try:
        target_ip_index = int(input(f"\nEnter an option 1 - {len(ips)}, or 0 to Exit the script: "))
        break
    except ValueError:
        os.system('clear')
        print("Invalid input. Please enter an integer.\n")

if target_ip_index == 0:
    print("Exiting ... ")
    exit()
nmap(ips[target_ip_index - 1])

