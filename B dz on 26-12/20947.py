from itertools import *
graf = 'гб ба ав вд де еи иг бв жг жи жд'.split()
matr = '267 157 468 356 248 134 12 35'.split()
print(*range(1, 9))
for i in permutations('абвгджеи'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
        print(24+15)