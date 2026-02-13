from math import *
for N in range(1, 10**9):
    L = 172
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 356984 >= 54 * 2**20:
        print(N)
        break
# 129