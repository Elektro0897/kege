from itertools import *
def f(x):
    b = 36 <= x <= 75
    c = 60 <= x <= 110
    a = a1 <= x <= a2
    return (not a) <= (b == c)
line_x = [40, 61, 76]
line_a = [36, 60, 75, 110]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(min(ans))
#74