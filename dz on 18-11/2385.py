x = 16**820 - 2**761 +14
cnt0 = 0
while x:
    if x % 4 == 0:
        cnt0 += 1
    x //=4
print(cnt0)
print('ответ: 378')