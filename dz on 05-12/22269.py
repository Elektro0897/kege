from string import printable as alf
def conv(num, sys):
    res = ''
    while num:
        res += alf[num % sys]
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = conv(n, 5)
    if int(r) % 10 == 0:
        r.replace('1', '*')
        r.replace('4', '1')
        r.replace('*', '4')
        r = '33' + r
    else:
        r = r +'42'
        r = r[:-1] + '3'
    r = int(r, 5)
    if r < 1922:
        ans.append([r, n])
print(max(ans))
print('неправильный ответ: 74')