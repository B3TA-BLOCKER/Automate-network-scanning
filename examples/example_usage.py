from network_scanner.main import network_interface_info, get_local_network_info, nmap


def main():
    print("Network Interface Info:")
    print(network_interface_info())

    print("\nLocal Network Info:")
    print(get_local_network_info())


if __name__ == "__main__":
    main()