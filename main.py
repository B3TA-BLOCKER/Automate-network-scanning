# Author : B3TA-BLOCKER
# Github: https://github.com/B3TA-BLOCKER


#!/usr/bin/python 

# impoting the required  moudles
import os
import subprocess
import psutil  # provides an easy way to interact with system and process utilities


def network_interface_info():

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
            print("\n\n\t\t\t\tChoose One of the foillowing Network Interface :")
            for i in range(iterations):
                print(f"\t\t\t\t{i+1}. {list_of_interfaces_running[i]}")
            try:
                choice = int(input("\n\t\t\t\t -> "))
                
                if choice > iterations or choice < 1:
                    os.system('clear')
                    print("\n\t\t\t\tWrong Entry Try Again !!!! ")
                else:
                    break   
            except ValueError:
                # Handle the case where the input is not an integer
                os.system('clear')
                print("\n\t\t\t\tInvalid input. Please enter an integer.")
    return list_of_interfaces_running[choice - 1]



def get_local_network_info() :

    """Gets Subnet"""
    interface = network_interface_info()
    command = f"ifconfig {interface} | grep -A 1 'inet ' | awk '$1 == \"inet\" {{print $2}}'"
    local_ip = subprocess.check_output(command, shell=True).decode('utf-8').strip()
    subnet = '.'.join(local_ip.split('.')[:-1]) + '.0/24'
    print(subnet)


os.system('clear')
get_local_network_info()
