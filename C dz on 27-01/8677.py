def f(x):
    return (x % 17 == 0) <= (not(x in range(80, 101))) or (a < x + 30)
ans = []
for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        ans.append(a)
print(max(ans))