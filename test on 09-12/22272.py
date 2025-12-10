def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for n in range(1, 100000):
    r = convert(n, 9)
    if r[0] == 7:
        r = r.replace('6', '*')
        r = r.replace('3', '6')
        r = r.replace('*', '3')
        r = '34' + r
    else:
        r = '3' + r[1:] + '45'
    r = int(r, 9)
    if r < 2876:
        print(n, r)