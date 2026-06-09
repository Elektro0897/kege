from math import *
for L in range(1, 10**9):
    i = ceil(log2(10 + 27))
    I = ceil(L * i / 8)
    if I * 3548 > 12 * 2**10:
        print(L)
        break
# 5