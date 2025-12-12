from itertools import permutations
k = 0
for val in set(permutations('ворота', r=6)):
    val = ''.join(val)
    val = val.replace('о', '*')
    val = val.replace('а', '*')
    if '**' not in val:
        k += 1
print(k)