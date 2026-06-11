from itertools import *
s = sorted('цитрус')
k = 0
for pos, val in enumerate(product(s, repeat=5), start=1):
    val = ''.join(val)
    if val.count('и') == 2 and 'цц' not in val:
        k = pos
print(k)
# 7525