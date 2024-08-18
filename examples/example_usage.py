import sys
import os

# Add the root directory of the project to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from network_scanner.main import network_interface_info, get_local_network_info, nmap


def main():
    print("Network Interface Info:")
    print(network_interface_info())

    print("\nLocal Network Info:")
    print(get_local_network_info())

    print("\nRunning Nmap Scan on 192.168.1.1:")
    nmap("192.168.1.1")

if __name__ == "__main__":
    main()
