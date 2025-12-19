from itertools import *

graf = 'af fe ec cg gd db ba fb ed'.split()
matr = '256 134 267 27 16 135 34'.split()

print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
