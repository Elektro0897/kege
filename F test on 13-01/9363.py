from itertools import *
k = 0
for val in permutations('х*ч*н*б*дж*т'):
    val = ''.join(val)
    if '*****' not in val:
        k += 1
print(k)