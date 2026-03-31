from ipaddress import *
net = ip_network('112.160.0.0/12')
k = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 3 != 0:
        k += 1
print(k)