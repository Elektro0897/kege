from itertools import *
graf = 'de ea ah hc cf fg gb bd eb hg'.split()
matr = '38 58 146 36 27 347 568 127'.split()
print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)