from math import *
for L in range(1, 10**10):
    i = ceil(log2(10 + 17))
    I = ceil(L * i / 8)
    if I * 7564230 > 31 * 2**20:
        print(L)
        break