from itertools import *
graf = 'ав вд де еи иг гб ба бв жд жи жг'.split()
matr = '267 157 468 356 248 134 12 35'.split()
print(*range(1, 9))
for i in permutations('абвгдежи'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
        # 39