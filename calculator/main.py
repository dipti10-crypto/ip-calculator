from calculator.ip_calc import calculate_network
from utils.validator import validate_ip

def main():
    ip = input("Enter IP Address: ")
    subnet = input("Enter Subnet (CIDR): ")

    if not validate_ip(ip):
        print("Invalid IP Address!")
        return

    try:
        subnet = int(subnet)

        result = calculate_network(ip, subnet)

        print("\n--- IP Calculation Result ---")
        print(f"Network Address  : {result['network_address']}")
        print(f"Broadcast Address: {result['broadcast_address']}")
        print(f"Total Hosts      : {result['total_hosts']}")
        print(f"Usable Hosts     : {result['usable_hosts']}")
        print(f"Subnet Mask      : {result['subnet_mask']}")
        print(f"CIDR             : /{result['cidr']}")
        print(f"First Host       : {result['first_host']}")
        print(f"Last Host        : {result['last_host']}")
       # print(f"All Hosts        : {result['all_hosts']}")

    except ValueError:
        print("Invalid subnet!")

if __name__ == "__main__":
    main()