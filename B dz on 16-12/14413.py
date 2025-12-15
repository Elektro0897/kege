from itertools import *
k = 0
for val in permutations('сортировка'):
    val = ''.join(val)
    for i in val:
        if i in 'сртвк':
            val = val.replace(i, '*')
        else:
            val = val.replace(i, '+')
    if '***' not in val and '+++' not in val:
        k += 1
        print(val)
print(k)