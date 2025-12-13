def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
k = 0
for n in range(1, 100000):
    r = convert(n, 7)
    if int(sum(map(int, r))) % 2 == 0:
        r = r + '555'
    else:
        r = '33' + r + '6'
    r = int(r, 7)
    if r < 12717:
        k = n
print(k)