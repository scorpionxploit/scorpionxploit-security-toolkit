"""
ScorpionXploit Security Toolkit - Subnet Calculator
Author: Aditya Sharma (scorpionxploit)
License: MIT
"""
import ipaddress
from typing import Dict, Any

def calculate_subnet(cidr: str) -> Dict[str, Any]:
    net = ipaddress.ip_network(cidr, strict=False)
    hosts = list(net.hosts())
    return {
        "network_address": str(net.network_address),
        "netmask": str(net.netmask),
        "broadcast_address": str(net.broadcast_address),
        "total_addresses": net.num_addresses,
        "usable_hosts": len(hosts),
        "first_usable": str(hosts[0]) if hosts else None,
        "last_usable": str(hosts[-1]) if hosts else None,
    }
