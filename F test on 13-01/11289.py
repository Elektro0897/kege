from itertools import *
from string import printable as alf
k = 0
for val in permutations(alf[:9], r=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('2') == 0:
        for i in '1357':
            val = val.replace(i, '*')
        for i in '24680':
            val = val.replace(i, '+')
        if '**' not in val and '++' not in val:
            k += 1
print(k)