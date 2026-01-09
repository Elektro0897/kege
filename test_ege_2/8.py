from itertools import *
from string import printable as alf
cnt = 0
for x in product(alf[:25], repeat=4):
    x = ''.join(x)
    for i in alf[1:25:2]:
        x = x.replace(i, '*')
    for m in alf[:25]:
        if int(m, 25) <= 5:
           x = x.replace(m, '+')
    if x.count('+') <= 2 and x.count('*') == 1:
        cnt += 1
print(cnt)