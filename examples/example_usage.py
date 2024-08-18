from network_scanner.scanner import network_interface_info, get_local_network_info, nmap_scan

def example():
    interfaces = network_interface_info()
    if not interfaces:
        print("No network interfaces found!")
        return

    interface = interfaces[0]  # Example usage with the first interface
    subnet = get_local_network_info(interface)
    print(f"Scanning subnet: {subnet}")
    ips = nmap_scan(subnet)
    print("Discovered IPs:")
    for ip in ips:
        print(ip)

if __name__ == "__main__":
    example()
