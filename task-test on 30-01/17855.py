from itertools import *
graf = 'ec ca ab bd df fe gc gf gd'.split()
matr = '457 46 567 12 136 235 13'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
        #38