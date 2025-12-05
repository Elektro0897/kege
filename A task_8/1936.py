from itertools import *
k = 0
for val in product('пскаль', repeat=4):
    val = ''.join(val)
    if val[0] != 'ь' and 'ьь' not in val:
        k += 1
print(k)