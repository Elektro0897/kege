from itertools import *
graf = 'fc cg ga ad db bf eb ef ec eg'.split()
matr = '47 357 2567 16 236 345 123'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)