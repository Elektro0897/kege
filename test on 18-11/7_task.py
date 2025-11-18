for n in range(1,100000):
    r = f'{n:3}'
    print(r)
    if n % 2 == 0:
        r = r + r[-2:]
    else:
        r = r + str(sum(map(int, r)))
    if n > 9:
        print(r)
        break