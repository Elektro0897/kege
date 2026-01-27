def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for p in range(int(max('boomblcng'), 36) + 1, 37):
    num1 = int('bo', p)
    num2 = int('om', p)
    num3 = int('bl4', p)
    num4 = int('cng', p)
    num5 = num1 + num2 + num3
    if num5 == num4:
        print(p)
        #34