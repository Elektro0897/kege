from string import printable as prin
from itertools import permutations as per
k = 0
for val in set(per(prin[:10], r=6)):
    val = ''.join(val)
    if val[0] != '0' and int(val) % 4 == 0:
        for i in '02468':
            val = val.replace(i, '*')
        if '**' not in val:
            k += 1
print(k)
