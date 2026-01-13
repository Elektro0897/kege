from itertools import *
graf = 'ac ce eg gf fd db ba bc de'.split()
matr = '67 567 457 35 234 12 123'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)