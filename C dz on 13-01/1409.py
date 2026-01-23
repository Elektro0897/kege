from itertools import *
def f(x):
    p = 23 <= x < 45
    q = 34 <= x <= 56
    a = a1 <= x <= a2
    return (not a) or (not p) and q
line_a = [23, 34, 45, 56]
line_x = [23, 35, 46]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(max(ans))
#11