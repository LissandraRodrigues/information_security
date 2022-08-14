import ipaddress

# ip = '192.168.0.1'
ip = '192.168.0.0/24'

# address = ipaddress.ip_address(ip)

network = ipaddress.ip_network(ip, strict=False)

for ip in network:
    print(ip)
