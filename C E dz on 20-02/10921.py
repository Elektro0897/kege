from itertools import *
cnt = 0
for val in set(permutations('джаваскрипт')):
    val = ''.join(val)
    k = 0
    for i in range(len(val)):
        if val[i] in 'аи':
            k += i
    if k == 11:
        cnt += 1 + 1
print(cnt)