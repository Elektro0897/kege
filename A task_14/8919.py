ans = 0
for x in range(1, 3000):
    num = 12*19**12 + 9*19**9 + 5*19**5 - x
    k = 0
    while num:
        if num % 19 == 0: k += 1
        num //= 19
    if k % 2 == 0:
        ans += x
print(ans)
#455221