from sys import setrecursionlimit
setrecursionlimit(10000)
def f(n):
    if n < 10:
        return n
    if n >= 10:
        return 3 * n + f(n-3)
    return None
print((f(6250) + 2 * f(6244))/f(6238))