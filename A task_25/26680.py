def prost(num):
    if num < 2: return False
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            return False
    return True

def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i**2 < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]
    return d
k = 0
for n in range(5000001, 10**10, 2):
    d = fact(n)
    if len(set(d)) == 2 == len(d) and prost(d[1] - d[0]):
        print(n, d[1])
        k += 1
        if k == 5:
            break

# 5008643 2239
# 5143823 2269
# 5336099 2311
# 5475599 2341
# 5673923 2383