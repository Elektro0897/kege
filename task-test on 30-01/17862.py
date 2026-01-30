from itertools import *
from string import printable as alf
k = 0
for val in product(alf[:12], repeat=5):
    val = ''.join(val)
    if val.count('7') == 0:
        for i in alf[9:12]:
            val.replace(i, '+')
        if val.count('+') <= 3:
            k += 1
print(k)