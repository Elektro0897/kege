from functools import lru_cache

def f(n):
    if n > 30: return f(n-6) + 2048
    return 3 * (g(n-5) + 13)

@lru_cache(None)
def g(n):
    if n >= 221337: return 2 * n + 50
    return g(n+11) - 48

for i in range(221500, 0, -1):
    g(i)

print(f(5078))
#155371