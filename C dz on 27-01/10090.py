from itertools import *
from string import printable as alf
k = 0
for val in permutations(alf[:8], r=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('1') == 0:
        for i in alf[:8:2]:
            val = val.replace(i, '+')
        for i in alf[1:8:2]:
            val = val.replace(i, '*')
        if '**' not in val and '++' not in val:
            k += 1
print(k)
#180