from itertools import *
k = 0
for val in permutations('кайф', r=4):
    val = ''.join(val)
    if val[-1] != 'й' and 'кф' not in val:
        k += 1
print(k)