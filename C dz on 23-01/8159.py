def f(x, y):
    b = 50 <= x <= 70
    return (2 * x + y != 150) or (not b) or (a > y)
ans = []
for a in range(0, 1000):
    if all(f(x, y) for x in range(0, 300) for y in range(0, 300)):
        ans.append(a)
print(min(ans))
#51?
#да