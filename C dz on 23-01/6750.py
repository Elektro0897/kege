def f(x, y):
    return (x + y <= 32) or (y <= x + 4) or (y >= a)
ans = []
for a in range(0, 1000):
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        ans.append(a)
print(max(ans))
#19