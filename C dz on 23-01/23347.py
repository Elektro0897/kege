from string import printable as alf
def convert(num, sys):
    res = ''
    while num:
        res += alf[num % sys]
        num //= sys
    return res[::-1]
val = convert(15 * 49**237 + 37 * 343**500 - 14 * 7**35, 49)
k = 0
for val in alf[15:49]:
    k += 1
print(k)