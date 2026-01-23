from itertools import *
from string import printable as alf
k = 0
for x in permutations(alf[:8], r=6):
    x = ''.join(x)
    if int(x, 8) % 5 == 0 and x[0] != '0':
        for i in alf[:8:2]:
            x = x.replace(i, '+')
        for i in alf[1:8:2]:
            x = x.replace(i, '*')
        if '**' not in x and '++' not in x:
            k += 1
print(k)
#208