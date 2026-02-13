from math import *
L = 101
N = 10 + 4090
i = ceil(log2(N))
I = ceil(L * i / 8)
print(I * 2048 // 2 ** 10)
#330