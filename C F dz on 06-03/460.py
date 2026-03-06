def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
k = 0
for a in range(10_000, 100_000):
    for b in range(10_000, 100_000):
        if a > b:
            c = int(convert(a, 5)) - int(convert(b, 5))
            if c:
                k += 1
print(k)