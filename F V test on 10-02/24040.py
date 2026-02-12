from math import *
for L in range(1, 1000)[::-1]:
    N = 52 + 1989 + 10
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 836 * I <= 639 * 2 ** 10:
        print(L)
        break
#521? da