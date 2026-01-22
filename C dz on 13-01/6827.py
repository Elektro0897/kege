from itertools import *
def f(x):
    p = 257 <= x <= 1000
    q = 5 <= x <= 100
    r = 99 <= x <= 258
    a = a1 <= x <= a2
    return (x <= r) and ((not (a <= p)) <= q)
line_a = [5, 99, 100, 257, 1000]
line_x = [6, 99.5, 101, 258]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(ans)
#0? []