from itertools import *
graf = 'be ef fd dc ca ag gb ba fc'.split()
matr = '246 16 57 15 347 127 356'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)