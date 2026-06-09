from math import *
for N in range(1, 10**9):
    i = ceil(log2(N))
    I = ceil(172 * i / 8)
    if I * 356984 >= 54 * 2**20:
        print(N)
        break
# 129