from itertools import *
def f(x):
    p = 10 <= x <= 150
    q = 160 <= x <= 250
    r = 240 <= x <= 300
    a = a1 <= x <= a2
    return (q <= p) or ((not a) <= r)
line_a = [10, 150, 160, 240, 250, 300]
line_x = [11, 151, 161, 241, 251]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(min(ans))