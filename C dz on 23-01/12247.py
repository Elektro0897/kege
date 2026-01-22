def f(x):
    return (x & a == 0) or (not(x & 37 == 0)) or (not(x & 12 == 0))
ans = []
for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        ans.append(a)
print(max(ans))
#45