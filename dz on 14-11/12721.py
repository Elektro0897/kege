def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
l = []
k = []
for n in range(80, 100000):
    r = convert(n, 8)
    for i in r:
        if int(i) % 2 == 0:
            k.append(i)
            if int(len(k)) % 2 != 0:
                r = r[-3:] + '46'
            else:
                r = str(convert((n % 8 * 5), 8)) + r
    r = int(r, 8)
    if n:
        l.append(r)
print(min(l))