def convert10(num, sys):
    num = num[::-1]
    k = 0
    for i in range(len(num)):
        k += int(num[i], 36)*sys**i
    return k
for p in range(33, 100):
    num1 = convert10('kot', p)
    num2 = convert10('golodni', p)
    num3 = convert10('meeow', p)
    num4 = convert10('100', p)
    if num1 + num2 == num3 * num4 - 20194023088:
        print(convert10('purr', p))
#1529685