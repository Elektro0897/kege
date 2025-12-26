from itertools import *
graf = 'bd de ea ac cg gb fg fc fe'.split()
matr = '26 147 456 237 37 13 245'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
        print(39+21)