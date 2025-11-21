from string import printable
def convert(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = convert(n, 3)
    sum1 = sum(map(int, r))
    if sum1 % 3 == 0:
        r += '212'
    else:
        sum1 *= 2
        t = convert(sum1, 3)
        r += t
    r = int(r, 3)
    if r > 490:
        ans.append(r)
print(min(ans))