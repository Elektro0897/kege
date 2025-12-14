def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
k = 0
for x in range(0, 3001):
    num1 = convert(9*11**210 + 8*11**150 - x, 11)
    if num1.count('0') == 60:
        k = x
print(k)