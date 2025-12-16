def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for x in range(1, 27001):
    num1 = 3*27**9 + 2*27**6 + 27**3 - x
    num1 = convert(num1, 27)
    if num1.count('0') == 6:
        print(x)