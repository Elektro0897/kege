from string import printable as alf
def convert(num, sys):
    res = ''
    while num:
        res += alf[num % sys]
        num //= sys
    return res[::-1]
res1 = 0
for x in range(1, 2031):
    num1 = convert(7**170 + 7**100 - x, 7)
    if num1.count('0') >= res1:
        res1 = num1.count('0')
        print(x)
print('ответ: 1715')