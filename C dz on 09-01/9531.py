from itertools import *
graf = 'аб бд де еж жз за ва вб вг гд ез'.split()
matr = '345 35 128 156 124 478 68 367'.split()
print(*range(1, 9), sep='')
for i in permutations('абвгдежз'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i, sep='')