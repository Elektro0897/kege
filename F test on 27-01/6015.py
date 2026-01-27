from string import printable as alf
from itertools import *
k = 0
for val in product(alf[:9], repeat=7):
    val = ''.join(val)
    if val.count('8') == 1 and val[0] != '0':
        for i in alf[:9:2]:
            val = val.replace(i, '+')
        for i in alf[1:9:2]:
            val = val.replace(i, '*')
    if val[0] != '*' and val[-1] != '+':
        k += 1
print(k)
#3521401
