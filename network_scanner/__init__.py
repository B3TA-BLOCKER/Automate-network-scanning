# __init__.py

"""
Automate Network Scanning Package

This package includes functionality for automating network scans
using tools like NetDiscover and Nmap. It interacts with system
utilities to gather network interface information and performs
scanning tasks based on user inputs.
"""

# Import key functions from main.py
from .main import bash, network_interface_info, get_local_network_info, nmap

# Define any package-level constants or settings here if needed
PACKAGE_NAME = "Automate Network Scanning"
