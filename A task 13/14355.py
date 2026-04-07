from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return str(ip)[:16].count('1') >= str(ip)[16:].count('1')

for mask in range(16, 25):
    net = ip_network(f'127.63.67.1/{mask}', False)
    if all(f(ip) for ip in net):
        print(net.netmask)
        break