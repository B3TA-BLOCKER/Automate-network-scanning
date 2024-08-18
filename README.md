# Automate Network Scanning 🚀

Welcome to **Automate Network Scanning** – a powerful Python tool designed to streamline the process of network discovery and port scanning. This tool automates the tedious tasks of discovering devices on your network and performing comprehensive port scans to identify open ports.

## Features 🌟

- **Automatic Network Discovery**: Identifies all active network interfaces and discovers devices on your local subnet.
- **Port Scanning**: Performs a detailed scan of all TCP ports on discovered devices to find open ports.
- **Intense Nmap Scan**: Runs an intensive Nmap scan on detected open ports and logs results.
- **User-Friendly Interface**: Interactive command-line interface to guide you through the scanning process.


## Documentation 📚

For detailed information on installation, usage, and configuration, please refer to the documentation:

- [Introduction](docs/index.md)
- [Installation Guide](docs/installation.md)
- [Usage Instructions](docs/usage.md)

## Example Usage 💡

Here's a brief example of how you might use the tool in a script:

```python
from network_scanner.scanner import network_interface_info, get_local_network_info, nmap_scan

def example_usage():
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
    example_usage()
```

## Contributing 🤝

I welcome contributions to improve this tool. If you'd like to contribute, please:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License 📜

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Contact 📫

For any questions or feedback, please reach out to [B3TA-BLOCKER](https://github.com/B3TA-BLOCKER).

Happy Scanning! 🔍
