import ipaddress

def calculate_network(ip, subnet):
    network = ipaddress.ip_network(f"{ip}/{subnet}", strict=False)

    hosts = list(network.hosts())

    first_host = hosts[0] if hosts else None
    last_host = hosts[-1] if hosts else None
    

    return {
        "network_address": network.network_address,
        "broadcast_address": network.broadcast_address,
        "total_hosts": network.num_addresses,
        "usable_hosts": max(network.num_addresses - 2, 0),
        "subnet_mask": network.netmask,
        "cidr": network.prefixlen,
        "first_host": first_host,
        "last_host": last_host,
       # "all_hosts": list(network.hosts())
    }