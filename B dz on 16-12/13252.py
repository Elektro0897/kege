from itertools import *
k = 0
for val in set(permutations('кидала', r=5)):
    val = ''.join(val)
    if 'аа' not in val:
        k += 1
print(k)