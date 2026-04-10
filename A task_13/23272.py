from ipaddress import *
net = ip_network('205.99.68.249/21', False)
print(net[-2])
print(list(net.hosts())[-1])
print(max(net.hosts()))