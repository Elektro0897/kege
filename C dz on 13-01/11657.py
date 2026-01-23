from itertools import *
from string import printable as alf
k = 0
for val in permutations(alf[:8], r=6):
    val = ''.join(val)
    if val[0] != '0' and val.count('3'):
        for i in alf[:8:2]:
            val = val.replace(i, '*')
        if '**' in val:
            k += 1
print(k)
#9324