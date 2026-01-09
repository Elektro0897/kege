def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
v = []
for x in range(10, 70000):
    num1 = 5**2025 + 5**400 - x
    num1 = convert(num1, 5)
    if num1.count('4') >= 1:
        v.append([num1.count('4'), x])
print(max(v))