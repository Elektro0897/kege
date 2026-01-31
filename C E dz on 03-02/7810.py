from itertools import *
k = 0
for val in product('м*сл*', repeat=6):
    val = ''.join(val)
    if val.count('*') == 1:
        k += 1
print(k)
#2916