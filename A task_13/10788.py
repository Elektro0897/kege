from ipaddress import *
ip_1 = ip_address('201.44.240.107')
ip_2 = ip_address('201.44.240.33')
k = 0
for mask in range(8, 31):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_2 in net.hosts() and ip_1 in net.hosts():
        if f'{int(net.network_address):032b}'.count('1') >= 5:
            k += 1
print(k)
#15