def f(x):
    b = 50 <= x <= 70
    return (x % a == 0) or (b <= (not(x % 16 == 0)))
ans = []
for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        ans.append(a)
print(max(ans))
#64