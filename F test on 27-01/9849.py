from string import printable as alf
from itertools import *
k = 0
for val in product(alf[10:16], repeat=6):
    val = ''.join(val)
    for i in 'ae':
        val = val.replace(i, '*')
    if val[0] != '*' and val[-1] != '*':
        k += 1
print(k)
#20736