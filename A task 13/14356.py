from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return str(ip)[:16].count('0') <= str(ip)[16:].count('0')

for a in range(256)[::-1]:
    net = ip_network(f'217.109.{a}.94/23', False)
    if all(f(ip) for ip in net):
        print(a)
        break