x = 283**382 + 9**15 + 2**3
cnt_b = 0
cnt_c = 0
while x:
    if x % 14 == 11:
        cnt_b += 1
    if x % 14 == 12:
        cnt_c += 1
    x //= 14
print(abs(cnt_b - cnt_c))