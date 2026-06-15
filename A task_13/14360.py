from ipaddress import *
ip_host = ip_address('153.202.16.37')
for mask in range(16, 31)[::-1]:
    net = ip_network(f'{ip_host}/{mask}', False)
    if ip_host in net.hosts():
        if ip_address('153.202.16.32') == net.network_address:
            print(sum(map(int, str(net.netmask).split('.')[-2:])))
            break