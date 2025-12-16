from itertools import *
from string import *
k = 0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    if val[0] != 0 and val.count('b') == 2:
        for i in '02468a':
            val = val.replace(i, '+')
        for i in '13579b':
            val = val.replace(i, '*')
    if '**' not in val and '++' not in val:
        k += 1
print(k)