from string import printable as alf
def convert(num, sys):
    res = ''
    while num:
        res += alf[num % sys]
        num //= sys
    return res[::-1]
k = 0
x = convert(3 * 17**777 + 15 * 17**250 - 6 * 17**100 + 2, 17)
for i in alf[1:17:2]:
    x = x.replace(i, '')
print(len(set(x)))