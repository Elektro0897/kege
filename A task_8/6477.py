from itertools import permutations as per
k = 0
for val in set(per('левиоса')):
    val = ''.join(val)
    if val[0] not in 'еиоа' and val[len(val)//2] not in 'лвс':
        k += 1
print(k)

