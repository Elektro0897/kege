def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
x = 4*625**9 - 25**15 + 2*5**11 - 7
print(convert(x, 5).count('4'))
####################################
x = 4*625**9 - 25**15 + 2*5**11 - 7
cnt_4 = 0
while x:
    if x % 5 == 4:
        cnt_4 += 1
    x //= 5
print(cnt_4)