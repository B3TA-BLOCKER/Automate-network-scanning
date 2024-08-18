<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<p align="center">
  <h1 align="center">Automate Network Scanning 🚀</h1>
</p>



<p align="center">
  <strong>A powerful Python tool designed to streamline the process of network discovery and port scanning. This tool automates the tedious tasks of discovering devices on your network and performing comprehensive port scans to identify open ports.</strong>
</p>


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## Features 🌟

- **Automatic Network Discovery**: Identifies all active network interfaces and discovers devices on your local subnet.
- **Port Scanning**: Performs a detailed scan of all TCP ports on discovered devices to find open ports.
- **Intense Nmap Scan**: Runs an intensive Nmap scan on detected open ports and logs results.
- **User-Friendly Interface**: Interactive command-line interface to guide you through the scanning process.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## Project Structure 📂

```
Automate-network-scanning
   ├── LICENSE
   ├── README.md
   ├── docs
   │   ├── index.md
   │   ├── installation.md
   │   └── usage.md
   ├── examples
   │   └── example_usage.py
   ├── network_scanner
   │   ├── __init__.py
   │   ├── main.py
   │   ├── scanner.py
   │   └── utils.py
   ├── requirements.txt
   ├── setup.py
   └── tests
       ├── test_import.py
       ├── test_main.py
       ├── test_scanner.py
       └── test_utils.py
```

- **`LICENSE`**: License file for the project.
- **`README.md`**: This file containing an overview and instructions.
- **`docs/`**: Documentation files, including installation and usage guides.
- **`examples/`**: Example scripts demonstrating how to use the tool.
- **`network_scanner/`**: Core package of the project containing the main functionality.
  - **`__init__.py`**: Initializes the package.
  - **`main.py`**: Contains primary functions for network scanning.
  - **`scanner.py`**: Additional scanning-related functions.
  - **`utils.py`**: Utility functions used across the package.
- **`requirements.txt`**: Lists Python dependencies.
- **`setup.py`**: Setup script for installing the package.
- **`tests/`**: Unit tests for various components of the project.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## Documentation 📚

For detailed information on installation, usage, and configuration, please refer to the documentation:

- [Introduction](docs/index.md)
- [Installation Guide](docs/installation.md)
- [Usage Instructions](docs/usage.md)

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## Example Usage 💡

Here's a brief example of how you might use the tool in a script:

```python
from network_scanner.main import network_interface_info, get_local_network_info, nmap_scan

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

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## Contributing 🤝

I welcome contributions to improve this tool. If you'd like to contribute, please:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## License 📜

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## Contact 📫

For any questions or feedback, please reach out to [B3TA-BLOCKER](https://github.com/B3TA-BLOCKER).
