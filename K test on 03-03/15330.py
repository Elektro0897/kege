from itertools import *
def f(x):
    b = 24 <= x <= 90
    c = 47 <= x <= 115
    a = a1 <= x <= a2
    return c <= (((not a) and b) <= (not c))

line_a = [24, 47, 90, 115]
line_x = [25, 48, 91]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(min(ans))