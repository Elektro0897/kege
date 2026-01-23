from itertools import *
def f(x):
    b = 54 <= x <= 120
    c = 78 <= x <= 151
    a = a1 <= x <= a2
    return c <= ((b and (not a)) <= (not c))
line_a = [54, 78, 120, 151]
line_x = [55, 79, 121]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(min(ans))
#42