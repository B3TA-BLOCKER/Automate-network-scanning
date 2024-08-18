import subprocess
import psutil

def bash(command):
    try:
        return subprocess.check_output(command, shell=True).decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e.output.decode('utf-8')}")
        raise

def network_interface_info():
    interfaces = psutil.net_if_stats()
    return [interface for interface, stats in interfaces.items() if stats.isup]

def get_local_network_info(interface):
    local_ip = bash(f"ifconfig {interface} | grep -A 1 'inet ' | awk '$1 == \"inet\" {{print $2}}'")
    return '.'.join(local_ip.split('.')[:-1]) + '.0/24'

def nmap_scan(ip):
    return bash(f"nmap -T4 -p1-65535 {ip} | grep 'open'").splitlines()

def intense_scan(ip, port_list):
    bash(f"nmap -T4 -A -sV -p{port_list} -oN output.txt {ip}")
    print(f"Nmap Intense scan results logged in output.txt")
