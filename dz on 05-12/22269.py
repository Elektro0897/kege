def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = conv(n, 5)
    if r[-1] == '0':
        r = '33' + r.replace('1', '*').replace('4', '1').replace('*', '4')
    else:
        r = '3' + r[1:] + '42'
    r = int(r, 5)
    if r == 497:
        ans.append([r, n])
max_r = max(ans)[0]
all_n = []
for r, n in ans:
    if r == max_r:
        all_n.append(n)
print(min(all_n))