from string import printable as alf
from itertools import *
k = 0
for val in product(alf[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        new_v = ''
        for i in val:
            if int(i, 12) % 3 == 0:
                new_v += '*'
            else:
                new_v += '+'
        if '*+*+*+*' in new_v or '+*+*+*+' in new_v: # скорее всего из-за этой строки
            k += 1
print(k)
# оооочень долго грузит