from itertools import *
def f(x):
    p = 5 <= x <= 280
    q = 295 <= x <= 400
    r = 375 <= x <= 450
    a = a1 <= x <= a2
    return (q <= p) or ((not a) <= r)

line_a = [5, 280, 295, 375, 400, 450]
line_x = [6, 281, 296, 376, 401]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(min(ans))
#80