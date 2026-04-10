from ipaddress import *
ip = ip_address('218.48.192.56')
k = 0
for mask in range(22, 16, -1):
    net = ip_network(f'218.48.192.0/{mask}', False)
    if ip in net:
        k += 1
print(k)