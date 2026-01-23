from itertools import *
def f(x):
    p = 13 <= x <= 19
    q = 17 <= x <= 23
    a = a1 <= x <= a2
    return (not ((not p) <= q)) <= (a <= ((not q) <= p))
line_a = [13, 17, 19, 23]
line_x = [14, 18, 20]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(max(ans))
#10