from itertools import *
from string import *
k = 0
for val in product(printable[:16], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('9') == 1:
        print(val)
        for i in printable[:16:2]:
            val = val.replace(i, '*')
        for i in printable[1:16:2]:
            val = val.replace(i, '+')
        print(val)
        if '**' not in val and '++' not in val:
            k += 1
            print(val)
print(k)
#1680