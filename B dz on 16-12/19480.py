from itertools import *
k = 0
for val in permutations('парижанка'):
    val = ''.join(val)
    if val.count('аа') == 1 and val.count('иа') == 1 and val.count('аи') == 1:
        k += 1
print(k)