def f(s, k):
    if k == 15: return {s}
    return f(s + 10, k + 1) | f(s - 5, k + 1)

print(len(f(1, 0)))

##############################################################

def f1(s, k):
    if k == 15:
        ans.add(s)
        return
    f1(s + 10, k + 1)
    f1(s - 5, k + 1)

ans = set()
f1(1, 0)
print(len(ans))

##############################################################

num = {1}
for i in range(15):
    num = {x + 10 for x in num} | {x - 5 for x in num}

print(len(num))
