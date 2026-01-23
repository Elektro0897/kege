from itertools import *
def f(x):
    b = 20 <= x <= 80
    a = a1 <= x <= a2
    return b <= ((x % 17 == 0) <= a)
line_a = [20, 80]
line_x = [30]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(min(ans))
#60