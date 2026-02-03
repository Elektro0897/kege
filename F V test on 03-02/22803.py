from itertools import *
graf = 'ab bg ge ef fa da df dc ce cb'.split()
matr = '457 567 45 136 123 247 126'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
print('ответ:', 9 + 2)