def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for x in range(1, 2031)[::-1]:
    num1 = convert(7**170 + 7**100 - x, 7)
    if num1.count('0') == 71:
        print(x)
        break