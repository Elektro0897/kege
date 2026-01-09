from itertools import *
from string import printable as alf
k = 0
for i in product(alf[:9], repeat=7):
    if i[0] not in alf[1:9:2] and i[-1] not in '36' and i.count('6') >= 1:
        k += 1
print(k)