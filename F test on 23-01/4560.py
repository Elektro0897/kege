from itertools import *
k = 0
for val in permutations('тихорецк', r=4):
    val = ''.join(val)
    if sum(val[i] == 'тихо'[i] for i in range(4)) == 2:
        for i in 'иое':
            val = val.replace(i, '*')
        if val.count('*') == 2:
            k += 1
print(k)
#60