from itertools import *
graf = 'gf fe ed da ag ba bg bc cd'.split()
matr = '26 147 456 236 37 134 25'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
print(9+17)