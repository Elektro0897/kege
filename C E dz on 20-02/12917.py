from itertools import *
k = 0
for val in set(permutations('просто')):
    val = ''.join(val)
    if 'оо' not in val:
        k += 1
print(k)