def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
k = 0
for n in range(1, 100000):
    r = convert(n, 4)
    if r[0] == 3:
        r = r.replace('1', '-')
        r = r.replace('3', '1')
        r = r.replace('-', '3')
    else:
        r = '1' + r[1:] + '12'
    if int(r, 4) < 598:
        k = n
print(k)