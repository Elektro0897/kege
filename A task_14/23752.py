from string import printable as alf
def convert(num, sys):
    res = ''
    while num:
        res += alf[num % sys]
        num //= sys
    return res[::-1]

x = 2*2187**2020 + 729**2021-2*243**2022 + 81**2023 - 2*27**2024 - 6561
cnt = 0
num27 = convert(x, 27)
for i in num27:
    if int(i, 27)>9:
        cnt += 1
print(cnt)

cnt1 = 0
num27 = convert(x, 27)
for i in alf[10:27]:
        cnt1 += num27.count(i)
print(cnt1)

cnt2 = 0
num27 = convert(x, 27)
for i in num27:
    if i in alf[10:27]:
        cnt2 += 1
print(cnt2)
