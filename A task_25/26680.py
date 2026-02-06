def fact_1(num):
    d = []
    for i in range(2, int(num ** .5) + 1):
        while num % i == 0:
            d += [i]
            num // i

    if num > 2:
        d += [num]
    return d

def fact_2(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num // 2
    for i in range(3, int(num ** .5) + 1, 2):
        while num % i == 0:
            d += [i]
            num // i

    if num > 2:
        d += [num]
    return d

def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num // 2
    i = 3
    while i**2 < num:
        while num % i == 0:
            d += [i]
            num // i
        i += 2

    if num > 2:
        d += [num]
    return d