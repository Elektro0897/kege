from itertools import *
def f(x):
    p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    r = {12, 24, 36, 48, 60}
    a = a1 <= x <= a2
    return (not a) <= ((p and q) <= r)
line = [2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 27, 30, 36, 48, 60]
ans = []
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 * a1)
print(min(ans))
#120