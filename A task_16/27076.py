from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 43: return g(n+4)
    return 2 * f(n-2) - f(n-4) + 2
@lru_cache(None)
def g(n):
    if n < 11240: return g(n+3) + 2
    return q(n)
@lru_cache(None)
def q(n):
    if n < 21: return n + 4
    return q(n-4) + 2
for i in range(20, 11_240):
    q(i)
for i in range(46, 11_240)[::-1]:
    g(i)
print(f(2026))
###########################################
f = [0] * 2050
g = [0] * 12000
q = [0] * 12000
for n in range(12000):
    if n < 21: q[n] = n + 4
    else: q[n] = q[n-4] + 2
for n in range(12000)[::-1]:
    if n < 11_240: g[n] = g[n+3] + 2
    else: g[n] = q[n]
for n in range(2050):
    if n < 43: f[n] = g[n+4]
    else: f[n] = 2 * f[n-2] - f[n-4] + 2
print(f[2026])