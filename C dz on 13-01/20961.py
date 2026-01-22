from itertools import *
def f(x):
    p = 15 <= x <= 142
    q = 38 <= x <= 167
    a = a1 <= x <= a2
    return not (not (q <= ((not a and p) <= (not q))))
line_a = [15, 38, 142, 167]
line_x = [16, 39, 143]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(min(ans))
#104
