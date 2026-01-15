from itertools import *
def DEL(n, m):
    return n % m == 0
def f(x):
    b = 70 <= x <= 90
    a = a1 <= x <= a2
    return (DEL(x, a) or (b <= (not DEL(x, 22))))
line_a = [70, 90]
line_x = [80]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(max(ans))
#20