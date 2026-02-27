from functools import lru_cache
@lru_cache(None)
def f(s, e, k):
    if s % 2 != 0: k += 1
    if s == e and k <= 4: return 1
    if s > e or k > 5: return 0
    return f(s + 2, e, k) + f(s + 3, e, k) + f(s * 2 + 1, e, k)

print(f(1, 625, 0))