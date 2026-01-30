from ipaddress import *
ip_net = ip_network('172.16.168.0/255.255.248.0')
k = 0
for ip in ip_net:
    if bin(int(ip))[2:].count('1') % 5 != 0:
        k += 1
print(k)
#1663