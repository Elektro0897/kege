from itertools import *
from string import *
k = 0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    ans = ''.join(val)
    for i in val:
        if int(i, 12) % 2 == 0:
            ans.replace(i, '+')
        else:
            ans.replace(i, '*')
    if val.count('b') == 2 and ('*+*+*+*' in ans or '+*+*+*+' in ans):
        k += 1
print(k)