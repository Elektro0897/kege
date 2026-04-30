from math import *
L = 257
N = 17 + 4080
i = ceil(log2(N))
I = ceil(L * i / 8)
print(I * 8388608 / 2**20)
#3344