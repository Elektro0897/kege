from itertools import *
graf = 'bh hf fd dc ce ea ab ah ge gf gc'.split()
matr = '247 148 578 126 38 47 136 235'.split()
print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)