from itertools import combinations
def f(x):
    b = (1, 2, 3, 4)
    c = (5, 6, 7, 8)
    a = a1 <= x <= a2
    return (not b) and (not c) or a
line = [1, 2, 3, 4, 5, 6, 7, 8]
ans = []
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(min(ans))
#7