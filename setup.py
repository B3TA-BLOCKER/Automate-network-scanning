from setuptools import setup, find_packages

setup(
    name="automate_network_scanning",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "psutil",
    ],
    entry_points={
        "console_scripts": [
            "automate-network-scanning = network_scanner.main:main",
        ],
    },
)
