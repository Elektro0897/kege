from itertools import *
def treug(n, m, k):
    if n + m > k and m + k > n and n + k > m:
        return True
    else:
        return False
def f(x):
    return not ((treug(x, 11, 18) == (not (max(x, 5) > 68))) and treug(x, a, 5))
ans = []
for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        ans.append(a)
print(max(ans))
#64