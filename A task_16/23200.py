from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 10: return n
    return 3 * n + f(n-3)
for i in range(0, 6500):
    f(i)

print((f(6250) + 2 * f(6244)) / f(6238))
#3
#############################################

f = [0] * 6300
for n in range(6300):
    if n < 10: f[n] = n
    else: f[n] = 3 * n + f[n-3]
print((f[6250] + 2 * f[6244]) / f[6238])