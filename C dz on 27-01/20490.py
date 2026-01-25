def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for x in range(1, 2006):
    num1 = convert(4**163 * 5 + 12**62 - x, 5)
    if num1.count('1') < num1.count('4'):
        ans.append(x)
print(max(ans))
#2000