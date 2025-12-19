from itertools import *

graf = 'dc cf fg ge ea ad ah hb hg bd bc'.split()
matr = '346 348 12 127 678 15 458 257'.split()

#print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)