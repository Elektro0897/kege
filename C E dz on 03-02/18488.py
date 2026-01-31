def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for x in range(1, 1000):
    num1 = convert(7**666 + 7**333 + 49**x - 343, 7)
    if num1.count('6') == 49:
        print(x)
        break
        #26