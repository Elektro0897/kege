num_10 = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
cnt = 0
while num_10:
    if num_10 % 5 == 0:
        cnt += 1
    num_10 //= 5
print(cnt)