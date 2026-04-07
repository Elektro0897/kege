from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return str(ip)[:16].count('1') >= str(ip)[16:].count('1')

for a in range(256)[::-1]:
    net = ip_network(f'116.242.{a}.26/27', False)
    if all(f(ip) for ip in net):
        print(a)
        break