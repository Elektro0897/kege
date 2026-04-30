from ipaddress import *
net = ip_network('68.203.243.87/255.255.224.0', False)
print(net[-2])
print(68+203+255+254)
#780