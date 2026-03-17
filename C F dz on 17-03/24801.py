def f(s, e):
    if s == e: return 1
    if s > e: return 0
    return f(s + 1, e) + f(s + 2, e) + f(s + 4, e) + f(s + 8, e)
ans = 0
s = sorted(range(24, 33))
for i in s:
    ans += f(16, i) * f(i, 48)
print(ans)