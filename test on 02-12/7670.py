c = 0
ans = []
for n in range(151, 100100):
    r = hex(n)[2:]
    r = r.replace('a', '1')
    cnt_chet = 0
    # while r:
    #     if int(r, 16) % 2 == 0:
    #         c += 1
    #     r = int(r, 16) //2
    # r = hex(n)[2:]
    # if c > 2:
    #     r += 'b'
    # else:
    #     r = 'f' + r
    # r = int(r, 16)
    # if r > 3500:
    #     print(n)
    for i in r:
        if int(r, 16) % 2 == 0:
            cnt_chet += 1
    if cnt_chet > 2:
        r = r + 'b'
    else:
        r = 'f' + r
    r = int(r, 16)
    if r > 3500:
        ans.append([n, r])
print(min(ans))