from string import printable as alf
def convert(num, sys):
    res = ''
    while num:
        res += alf[num % sys]
        num //= sys
    return res[::-1]
res1 = []
for x in range(2030, 0, -1):
    num1 = convert(3**100 - x, 3)
    if num1.count('0') == 1:
        print(x)
        break