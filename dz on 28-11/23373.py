def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
k = 0
x = convert(2*2401**525 + 3*343**524 - 4*49**523 + 5*49**522 - 6*7**521 - 35, 49)
for i in x:
    if int(i) <= 9:
        k += 1
print(k)
print(x)