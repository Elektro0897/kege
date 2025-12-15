from itertools import *
k = 0
for val in product('01', repeat=16):
    val = ''.join(val)
    if val.count('1') % 3 == 0:
        k += 1
print(k)