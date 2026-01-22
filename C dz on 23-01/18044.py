from itertools import *
def f(x):
    m = 32 <= x <= 68
    n = 54 <= x <= 76
    a = a1 <= x <= a2
    return (not (m or n)) == (not a)
line_a = [32, 54, 68, 76]
line_x = [33, 55, 69]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(min(ans))
#44